# To run on Laptop
```bash
docker-compose up
```
# Create a VM
1. Go to Google Cloud
2. Create instance
3. Boot disk
  - Operating system: Ubuntu
  - Version: Ubuntu 22.04 LTS
4. Advance options >> Security
  - Add manually generated SSH keys
  - Paste the public-key here
  - Please see https://www.youtube.com/watch?v=uWLxUcKNTUY

# Firewall rules
1. Go to compute engine
2. Select vm instance e.g. vm2
3. Select network instance e.g. nic0
4. Side menu firewall
5. Menubar create a firewall rule 
  - Name: dsi321_firewall_rule
  - Allow match: Allow
  - Targets: All instances in the network
  - Source filter: IPv4 ranges 
  - Source IPv4: 0.0.0.0/0
  - Protocols and port: allow all

# setup docker
``` bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
docker --version
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

## setup jupyter
```bash
# mkdir data_science && cd data_science
nano docker-compose.yml
docker-compose up -d
docker-compose ps
docker-compose logs jupyter
sudo chmod ugo+rwx notebooks/
```
