# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "web1" do |web1|
    web1.vm.box = "bento/ubuntu-16.04"
    web1.vm.network "private_network", ip: "172.28.128.3"
    web1.vm.hostname = "web1-node"
    web1.vm.provision "shell" do |s|
      s.path = "vmsetup.d/vmsetup.sh"
      s.args = ["web"]
    end
    web1.vm.provision "shell" do |s|
      s.path = "setup.d/setup.sh"
      s.args = ["web1"]
    end
    web1.vm.provision "shell", run: "always" do |s|
      s.path = "startup.d/startup.sh"
      s.args = ["web1"]
    end
    web1.trigger.before :destroy do
      run_remote "consul leave" # shutdown gracefully
    end
  end

  config.vm.define "web2" do |web2|
    web2.vm.box = "bento/ubuntu-16.04"
    web2.vm.network "private_network", ip: "172.28.128.6"
    web2.vm.hostname = "web2-node"
    web2.vm.provision "shell" do |s|
      s.path = "vmsetup.d/vmsetup.sh"
      s.args = ["web"]
    end
    web2.vm.provision "shell" do |s|
      s.path = "setup.d/setup.sh"
      s.args = ["web2"]
    end
    web2.vm.provision "shell", run: "always" do |s|
      s.path = "startup.d/startup.sh"
      s.args = ["web2"]
    end
    web2.trigger.before :destroy do
      run_remote "consul leave" # shutdown gracefully
    end
  end
  
  config.vm.define "db2" do |db2|
    db2.vm.box = "bento/ubuntu-16.04"
    db2.vm.network "private_network", ip: "172.28.128.5"
    db2.vm.hostname = "db2-node"
    db2.vm.provision "shell" do |s|
      s.path = "vmsetup.d/vmsetup.sh"
      s.args = ["db"]
    end
    db2.vm.provision "shell" do |s|
      s.path = "setup.d/setup.sh"
      s.args = ["db2"]
    end
    db2.vm.provision "shell", run: "always" do |s|
      s.path = "startup.d/startup.sh"
      s.args = ["db2"]
    end
    db2.trigger.before :destroy do
      run_remote "consul leave" # shutdown gracefully
    end
  end

  config.vm.define "db1" do |db1|
    db1.vm.box = "bento/ubuntu-16.04"
    db1.vm.network "private_network", ip: "172.28.128.4"
    db1.vm.hostname = "db1-node"
    db1.vm.provision "shell" do |s|
      s.path = "vmsetup.d/vmsetup.sh"
      s.args = ["db"]
    end
    db1.vm.provision "shell" do |s|
      s.path = "setup.d/setup.sh"
      s.args = ["db1"]
    end
    db1.vm.provision "shell", run: "always" do |s|
      s.path = "startup.d/startup.sh"
      s.args = ["db1"]
    end
    db1.vm.provision "shell", path: "setup.d/db1-setup.sh"
    db1.trigger.before :destroy do
      run_remote "consul leave" # shutdown gracefully
    end
  end

end
