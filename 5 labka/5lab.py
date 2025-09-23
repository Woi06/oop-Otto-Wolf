#tizim = [10, 5, 20, 1, 15]
# Бастапқы тізімді шығарамыз
#(f"Бастапқы тізім: {tizim}")
# Тізімді кері тәртіпте шығарамыз
#print(f"Кері тәртіптегі тізім: {tizim[::-1]}")

#number 2
#def tizim_suryptau(tizim):
 #   return sorted(tizim, key=abs)
#sandar = [10, -5, -2, 8, -12]
#suryptalgan_sandar = tizim_suryptau(sandar)
#print(f"Бастапқы тізім: {sandar}")
#print(f"Абсолюттік мәні бойынша сұрыпталған: {suryptalgan_sandar}")

#number3

def ozgertu(tizim):
    if len(tizim) >= 2:

        tizim[0], tizim[-1] = tizim[-1], tizim[0]
    return tizim
menim_tizimim = [10, 20, 30, 40, 50]
print(f"Бастапқы тізім: {menim_tizimim}")
ozgergen_tizim = ozgertu(menim_tizimim)
print(f"Ауыстырудан кейінгі тізім: {ozgergen_tizim}")

baska_tizim = ['алма', 'банан', 'апельсин']
print(f"\nБастапқы тізім: {baska_tizim}")
ozgertu(baska_tizim)
print(f"Ауыстырудан кейінгі тізім: {baska_tizim}")