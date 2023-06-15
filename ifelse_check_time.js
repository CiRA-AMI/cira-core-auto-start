ifelse = false

dayName =['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = dayName[new Date().getDay()]
print(day + "\n")

const time = new Date()

h = time.getHours()
print(h + "\n")

m = time.getMinutes()
print(m + "\n")

s = time.getSeconds()
print(s + "\n")


if(day == "Sunday" || day == "Wednesday") {
     if(h == 3 && m == 0 && s  < 5) {
          ifelse = true
     }
}
