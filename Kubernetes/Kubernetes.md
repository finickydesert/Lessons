kubernetes control via kublets and kube-proxy in a "cluster"
you control kubernetesthrough the kubernetes api server via kubectl
scheduler
controller manager
pod: container
manifest yaml file creates the way to be deployed
service yaml can be created as a load bolancer also expose the ops to the internet (like for a website)


commands
kubectl get nodes: list what nodes there are.
kubectl cluster-info: gives more info on what there is within the cluster. 
kubectl run: run the pod "kubectl run "pod" --image=theimmageyouwanttouse(:pourover) --port  whatever the port
kubectl describe pods (must be done in linux): discribes pod in detail 
kubectl delete pos "name of pd"
kubectl apply -f nameofmanifest.yaml
kubectl get deployment: get name of deplyment
kubectl edit deployment "name of deployment-deployment
