# multik8s-pythonwebapp
Python+Flask web application running locally in Kubernetes cluster using Minikube with Persistent Volume Claim for the Webapp.

Steps to run Python Application using Minikube:

- Install Kubectl
- Install  minikube (recommended to install Virtual env)
- Run *kubectl get pods* to check whether everything is working and looks finr
- Then do a *kubectl apply -f k8s/* to setup Kubernetes cluster and run Python application in it.
- *BOOM* its ready.


Commands

- kubectl get pods  - To get list of Pods
- kubectl get nodes - To get list of Nodes
- kubect get services - To get list of Services
- kubectl get pvc - To get list of Persistent Volume Claims
- kubectl get pv - To get list of Persistent Volumes
