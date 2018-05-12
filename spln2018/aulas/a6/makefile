p1:
	grep '\{.*?\}' -Pno camara_segredos_anotado.txt | \
		awk 'BEGIN{\
				FS=OFS=":"\
			}\
			{a[$$2][int($$1/135)]++; }\
			END{for(x in a){\
					for(y in a[x]){\
						print x,y, a[x][y]\
					}\
				};\
			}' > tmp
