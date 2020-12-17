$script = <<-SCRIPT
    echo 'cd /vagrant' >> /home/vagrant/.bashrc
    mkdir /home/vagrant/.bin/local

    apt update
    apt install make python3-pip  python3-venv -y
SCRIPT

Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.hostname = "cyberpunk2077-accessibility"
    config.vm.provider :virtualbox do |vb|
        vb.name = "cyberpunk2077-accessibility"
        vb.memory = 2048
        vb.cpus = 2
    end

    config.vm.provision "shell", inline: $script
end
