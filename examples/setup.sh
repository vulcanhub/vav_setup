# Set this to BCI home, installed by running install.py.
export BCI_HOME=<BCI home>

# Add vav_setup/bin to $PATH.
current_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
setup_dir=$( dirname "$current_dir" )
if [ -z "$PATH" ]; then
   export PATH=$setup_dir/bin
else
   export PATH=$setup_dir/bin:$PATH
fi

# Modify this to set Risc-V tool installation path.  Needed only if building SW locally.
export PATH=/tools/riscv/bin:$PATH

