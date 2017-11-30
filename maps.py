class Maps:
        
    def from_star(self,dataset,observation_time,Ra="00h00m00s",Dec="00d00m00s",color_mark="bo",plot_size=15,antenna_textsize=8,conti_color="coral",sea_color="aqua",longspan=30,latispan=30,antenna_text_use=False,long_use=True,lati_use=True,map_color=True,**keys):
        import numpy as np
        from mpl_toolkits.basemap import Basemap
        import matplotlib.pyplot as plt
	from datetime import datetime

	from astropy import units
        from astropy.coordinates import SkyCoord
	
 	spring_time = datetime(2017,3,20,19,29,0) 

	# reference  http://keisan.casio.jp/exec/system/1184726771
	Ten_longtude = 24.35

        print("[the vernal spring equinox]:")
	print(spring_time)

        dt_now = observation_time
	print("[Observation DateTime]:")
	print(dt_now)

	
	timedelta = dt_now-spring_time
	total_minutes = timedelta.days*24*60+timedelta.seconds/60
	minutes_nokori1 = total_minutes % 1436.112
	hosei=  0.25067682743*minutes_nokori1


        RaDec_SK = SkyCoord(Ra, Dec,frame='icrs')
	print("center_latitude = " +str(0+RaDec_SK.dec.degree))
	print("center_longtude = " +str(360+Ten_longtude-hosei+RaDec_SK.ra.degree))

        map = Basemap(projection='ortho',lat_0=RaDec_SK.dec.degree, lon_0=Ten_longtude-hosei+RaDec_SK.ra.degree)


        #1.coastline
	map.drawcoastlines()


        #2.continents,sea color
	if map_color:        	
		map.fillcontinents(color=conti_color,lake_color=sea_color)
		map.drawmapboundary(fill_color=sea_color)

        #3.lon_lat line
	if long_use:
		map.drawmeridians(np.arange(0, 360, longspan), labels = [0, 0, 0, 1],dashes=[4,2])

	if lati_use:
		map.drawparallels(np.arange(-90, 90, latispan), labels = [1, 0, 0, 0],dashes=[4,2])


        #4.equator line
	map.drawparallels([0],color="r",linewidth=3,dashes=[1000,1])
	map.drawparallels([0],color="b",linewidth=1,dashes=[1000,1])


	#5.antenna plot
	long=dataset['Long'].tolist()
	lati=dataset['Lati'].tolist()
	plot=dataset['plot'].tolist()
	sta=dataset.index.tolist()

	print("station numbers = "+str(len(plot)))			

       	for num in range(len(plot)):
		x,y = map(long[num],lati[num])
		
		if (str(plot[num]) == str('nan')):
			map.plot(x, y, color_mark, markersize=plot_size)
			
	 	else:
			map.plot(x, y, plot[num], markersize=plot_size)

	#6.antenna_text plot
	if antenna_text_use:
		x,y = map(long,lati)

		for name,xpt,ypt in zip(sta,x,y):
			plt.text(xpt+150000, ypt, name, fontsize=antenna_textsize,fontweight='bold')

 
        plt.show()



    def worldmap(self,dataset,color_mark="bo",plot_size=15,antenna_textsize=20,conti_color="coral",sea_color="aqua",longspan=5,longfontsize=15,latispan=5,latifontsize=15,antenna_text_use=False,long_use=True,lati_use=True,map_color=True,**keys):

	from mpl_toolkits.basemap import Basemap
	import matplotlib.pyplot as plt
	import numpy as np

	map = Basemap(**keys)

        #1.coastline
	map.drawcoastlines()

        #2.continents,sea color
	if map_color:        	
		map.fillcontinents(color=conti_color,lake_color=sea_color)
		map.drawmapboundary(fill_color=sea_color)

        #3.long_lati line
	if long_use:
		map.drawmeridians(np.arange(0, 360, longspan), labels = [0, 0, 0, 1], fontsize=longfontsize,dashes=[4,2])

	if lati_use:
		map.drawparallels(np.arange(-90, 90, latispan), labels = [1, 0, 0, 0], fontsize=latifontsize,dashes=[4,2])

  	#4.equator line
	map.drawparallels([0],color="r",linewidth=3,dashes=[1000,1])
	map.drawparallels([0],color="b",linewidth=1,dashes=[1000,1])

	#5.mark and Antentext plot

	long=dataset['Long'].tolist()
	lati=dataset['Lati'].tolist()
	plot=dataset['plot'].tolist()
	sta=dataset.index.tolist()

	print("station numbers = "+str(len(plot)))			

       	for num in range(len(plot)):
		x,y = map(long[num],lati[num])
		
		if (str(plot[num]) == str('nan')):
			map.plot(x, y, color_mark, markersize=plot_size)			
	 	else:
			map.plot(x, y, plot[num], markersize=plot_size)

	#6.antenna_text plot
	if antenna_text_use:
		x,y = map(long,lati)

		for name,xpt,ypt in zip(sta,x,y):
			plt.text(xpt+0.5, ypt, name, fontsize=antenna_textsize,fontweight='bold',bbox=dict(facecolor='yellow',alpha=0.5))

	plt.show()