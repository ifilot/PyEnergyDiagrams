from pyenergydiagram.energydiagram import ED

#
# Simple example script to show how to run the program
# 
# @author Ivo Filot <ivo@ivofilot.nl>
#

# construct PED
diagram = ED()
diagram.dimension = 20
diagram.offset = 2
diagram.space = 10

# add states
diagram.add_level(0,'Separated Reactants')
diagram.add_level(-5.4,'mlC1')
diagram.add_level(-15.6,'mlC2','last',) #Using 'last' it will be together with the previous level
diagram.add_level(28.5,'mTS1',color='g')
diagram.add_level(-9.7,'mCARB1')
diagram.add_level(-19.8,'mCARB2','last')
diagram.add_level(20,'mCARBX','last')

# add links between levels
diagram.add_link(0,1)
diagram.add_link(0,2)
diagram.add_link(2,3)
diagram.add_link(1,3)
diagram.add_link(3,4)
diagram.add_link(3,5)
diagram.add_link(0,6)

(plt, fig, ax) = diagram.plot()
plt.show()