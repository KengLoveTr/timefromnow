from django.shortcuts import render
def index(request):
    return render(request, "index.html")
def count(request):
    if request.method == "POST":
        current = request.POST['current']
        hour = request.POST['hour']
        minute = request.POST['minute']
        if hour != "" and minute != "":
            current = current.split(":")
            current[1] = current[1].lstrip("0")
            current[0] = current[0].lstrip("0")
            current[0] = int(current[0]) + int(hour)
            current[1] = int(current[1]) + int(minute)
            if int(current[0]) > 24:
                current[0] = int(current[0]) - 24
            if int(current[1]) >= 60:
                current[0] = int(current[0]) + 1
                current[1] = int(current[1]) - 60
            if 24 >= int(current[0]) >= 10 and 60 >= int(current[1]) >= 10:
                time = str(current[0]) + ":" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[0]) >= 0:
                time = "0" + str(current[0]) + ":" + str(current[1])
                return render(request, "index.html", {"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[1]) >= 0:
                time = str(current[0]) + ":0" + str(current[1])
                return render(request, "index.html", {"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[1]) >= 0 and 10 > int(current[0]) >= 0:
                time = "0" + str(current[0]) + ":0" + str(current[1])
                return render(request, "index.html", {"Current": current, "Hour": hour, "Minute": minute, "Time": time})
        elif hour == "" and minute != "":
            current = current.split(":")
            current[1] = current[1].lstrip("0")
            current[0] = current[0].lstrip("0")
            current[1] = int(current[1]) + int(minute)
            if int(current[1]) >= 60:
                current[0] = int(current[0]) + 1
                current[1] = int(current[1]) - 60
            if 24 >= int(current[0]) >= 10 and 60 >= int(current[1]) >= 10:
                time = str(current[0]) + ":" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[0]) >= 0:
                time = "0" + str(current[0]) + ":" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[1]) >= 0:
                time = str(current[0]) + ":0" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[1]) >= 0 and 10 > int(current[0]) >= 0:
                time = "0" + str(current[0]) + ":0" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})
        elif hour != "" and minute == "":
            current = current.split(":")
            current[1] = current[1].lstrip("0")
            current[0] = current[0].lstrip("0")
            current[0] = int(current[0]) + int(hour)
            if int(current[0]) >= 24:
                current[0] = int(current[0]) - 24
            if 24 >= int(current[0]) >= 10 and 60 >= int(current[1]) >= 10:
                time = str(current[0]) + ":" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[0]) >= 0:
                time = "0" + str(current[0]) + ":" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[1]) >= 0:
                time = str(current[0]) + ":0" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})
            elif 10 > int(current[1]) >= 0 and 10 > int(current[0]) >= 0:
                time = "0" + str(current[0]) + ":0" + str(current[1])
                return render(request, "index.html",{"Current": current, "Hour": hour, "Minute": minute, "Time": time})

