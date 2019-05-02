# Check for plugins
if !Vagrant.has_plugin?("vagrant-proxyconf") 
	system('vagrant plugin install vagrant-proxyconf')
end

if !Vagrant.has_plugin?("vagrant-vbguest") 
	system('vagrant plugin install vagrant-vbguest')
end

Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"
  config.vm.box_check_update = false

  config.vm.network "forwarded_port", guest: 12322, host: 8484

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"

  # Share an additional folder to the guest VM.
  config.vm.synced_folder "C:/FirstPy/", "/vagrant_cicd"
  
  config.vm.provider "virtualbox" do |vb|
  # Customize the amount of memory on the VM:
     vb.memory = "2056"
  end
  
  # Enable provisioning with a shell script.
  config.vm.provision "shell", inline: <<-SHELL
	
	#dependencies for docker
	yum install -y yum-utils \
	device-mapper-persistent-data \
	lvm2
	
	# download repo for docker
	yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
	
	# install docker
	yum install -y docker-ce epel-release
	systemctl enable docker.service
	systemctl start docker.service
	
	# update yum
	# yum install -y https://centos7.iuscommunity.org/ius-release.rpm
	yum update
	
  SHELL
end