```
kubectl create cm code --from-file=http_server.py
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```