import wolframalpha as wa


wolfkey = "AP3U23-4LY6VHLW57"
client = wa.Client(wolfkey)

query = "mechanical engineering equations"
query = "centripital motion equation"

qres = client.query(query)

print(qres)

# print(next(qres.results).text)


for pod in qres.pods:
    for sub in pod.subpods:
        print(sub.plaintext)









# END
