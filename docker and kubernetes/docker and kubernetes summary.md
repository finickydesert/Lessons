have a ubuntu vm on hand for this
i might bring it into a go file as a note like the notes i have for go. 

videos used:
prep vids: https://www.youtube.com/watch?v=eGz9DS-aIeY , https://www.youtube.com/watch?v=7bA0gTroJjw
actual vid: 

docker is a container or a program to contain aplications and OS's 
kubernetes is a controller of containers.

docker Commands (note all commands are uncap, it keeps getting autocorrected to cap) 

run: execute whatever “docker run ngnix”. If not there then it’ll go out and get it. 
ps: list all containers 
rm: remove container “docker rm “name of container” 
Images: see what images and sizes of those images “docker images” *don’t remove images if they are being used *you must stop and delete containers that use the image before deleting the image 

Kubernetes
kubernetes control via kublets and kube-proxy in a "cluster"
you control kubernetesthrough the kubernetes api server via kubectl
scheduler
controller manager

commands
kubectl get nodes: list what nodes there are.
kubectl cluster-info: gives more info on what there is within the cluster. 
