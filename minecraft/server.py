from minecraft.const import START_SCRIPT_PATH, mcsub

# start script args
# export ATM10_INSTALL_ONLY=true
# export ATM10_RESTART=false
# export ATM10_JAVA

def install():
    cmd = [START_SCRIPT_PATH, 'export ATM10_INSTALL_ONLY']
    result = mcsub(cmd)
    print(result)

