import utils.verifications as verify

# install on arch
def install_sdkman():
    verify.install_sdkman()
    
    verify.run_playbook('arch')


