from __future__ import print_function

import os
import uuid
import timeit
import argparse
import tempfile
import subprocess
import IPython.core.magic as ipym


def get_argparser():
    parser = argparse.ArgumentParser(description='CppMagic params')
    parser.add_argument("-t", "--timeit", action='store_true',
                        help='flag to return timeit result instead of stdout')
    parser.add_argument("rest", nargs = argparse.REMAINDER)
    return parser


@ipym.magics_class
class CppMagic(ipym.Magics):
    
    def __init__(self, shell):
        super(CppMagic, self).__init__(shell)
        self.argparser = get_argparser()
        
    def _compile(self, file_path, compilerOpts=None):
        cmd = ["g++", file_path + ".cpp", "-o", file_path + ".out"] + compilerOpts[1:len(compilerOpts)]
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)

    def _run(self, file_path, timeit=False):
        if timeit:
            stmt = "subprocess.check_output(['{}'], stderr=subprocess.STDOUT)".format(file_path + ".out")
            output = self.shell.run_cell_magic(magic_name="timeit", line="-q -o import subprocess", cell=stmt)
        else:
            output = subprocess.check_output([file_path + ".out"], stderr=subprocess.STDOUT)
            output = output.decode('utf8')
        return output
    
    @ipym.cell_magic
    def cpp(self, line, cell):
        try:
            args = self.argparser.parse_args(line.split())
        except SystemExit as e:
            self.argparser.print_help()
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, str(uuid.uuid4()))
            with open(file_path + ".cpp", "w") as f:
                f.write(cell)
            try:
                self._compile(file_path, compilerOpts = args.rest)
                output = self._run(file_path, timeit=args.timeit)
            except subprocess.CalledProcessError as e:
                print(e.output.decode("utf8"))
                output = None
        return output

def load_ipython_extension(ip):
    cpp_magic = CppMagic(ip)
    ip.register_magics(cpp_magic)

