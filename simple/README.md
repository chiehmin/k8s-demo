```
kubectl create cm --from-file=http_server.py
kubectl apply -f deploy.yml
kubectl apply -f svc.yml
```