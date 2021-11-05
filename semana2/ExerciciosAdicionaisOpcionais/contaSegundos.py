segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")

total_segs = int(segundos_str)

a = total_segs // (3600 * 24)
segs_restantes1 = total_segs % (3600 * 24)

b = segs_restantes1 // 3600                   
segs_restantes2 = segs_restantes1 % 3600   

c = segs_restantes2 // 60         
d = segs_restantes2 % 60    
print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")

