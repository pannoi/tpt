# HOWTO

>To run this application locally, need node and npm to be installed

* node - 

* npm - 

```bash
# Install dependencies for nodeJS
# Dependecies are described in package.json
npm install 

# Run application
node index.js

# Application works on 8081
firewall-cmd --permanent --zone=public --add-port=8081/tcp
firewall-cmd --reload
```