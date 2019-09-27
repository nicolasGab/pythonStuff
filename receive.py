from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np

client = MongoClient(port=27017)
db=client.db

worker_elapsed = db.time.find({"worker_elapsed":{"$exists":True}})
arr = []
for res in worker_elapsed:
    arr.append(int(res['worker_elapsed']))

Wmean = np.mean(arr)

# nparr = np.array(arr)
print("\nWorker response times")
print("mean ",Wmean)
print("q 0.25 ",np.quantile(arr, 0.25))
print("q 0.50 ",np.quantile(arr, 0.5))
print("q 0.75 ",np.quantile(arr, 0.75))
print("q 0.95 ",np.quantile(arr, 0.95))
print("q 0.99 ",np.quantile(arr, 0.99))

plt.hist(arr,100, label="worker")
plt.axvline(Wmean, c='c', ls='--', label='Worker mean '+str(round(Wmean))+' ms')


api_elapsed = db.time.find({"api_elapsed":{"$exists":True}})
apiarr = []
for res in api_elapsed:
    apiarr.append(int(res['api_elapsed']))

APImean = np.mean(apiarr)

# nparr = np.array(arr)
print("\nAPI Response times")
print("mean ",APImean)
print("q 0.25 ",np.quantile(apiarr, 0.25))
print("q 0.50 ",np.quantile(apiarr, 0.5))
print("q 0.75 ",np.quantile(apiarr, 0.75))
print("q 0.95 ",np.quantile(apiarr, 0.95))
print("q 0.99 ",np.quantile(apiarr, 0.99))

plt.hist(apiarr,100, label="API")
plt.axvline(APImean, c='r', ls='--', label='API mean '+str(round(APImean))+' ms')


plt.ylabel('count')
plt.xlabel('ms')
plt.title('response time')
plt.legend()
plt.show()