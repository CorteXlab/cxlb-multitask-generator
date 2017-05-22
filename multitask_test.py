#!/usr/bin/env python

# BEFORE USE :
# NOTE THAT YOU NEED EXECO IN ORDER TO RUN THIS FILE 
# http://execo.gforge.inria.fr/doc/latest-stable/

from execo import *
from execo_engine import *
from node_type import node_type
from string import Template
import os

class benchmark(Engine):

    def run(self):

	if not os.path.exists('Benchmark'):
    		os.makedirs('Benchmark')
	os.chdir('Benchmark')
	####################################################################################################################
	## in ../Benchmark/
	####################################################################################################################
	benchdir_0 = os.getcwd()

	#Here we have only one testing parameter (node id), so number of steps N is the number of targeted nodes
	#if you add n other paramaters which have M(n) possible values, number of steps is M(1)xM(2)x...xM(n)xN (Cartesian product)	 
	
        combs = {
            "node": [i for i in range(1,41)],
	    #"bench_type": ["benchA", "benchB"],
            #"freq": [ 500, 1000, 2000],
            #"gain": [-10, -50, -70, -40]
        }
        sweeps = sweep(combs)
        sweeper = ParamSweeper(self.result_dir, sweeps)

        while len(sweeper.get_remaining()) > 0:

		#For each Tx node 

		os.chdir(benchdir_0)		#Each loop step starts in ../Benchmark/
		comb = sweeper.get_next()

		nodeid = comb['node']
		nodetype = node_type(nodeid)

		# Do something with the comb
		"""print "combinaison traitee: %s" % (comb,)
		print "node: mnode%i" % (nodeid)
		print "type : " + nodetype
		#print "bench: %s" % (comb['bench_type'])
		"""
		count=40
		s_rx=""
		
		#if nodetype != "NaN" :		# USRP exclusive here
		if nodetype == "USRP" :

		#Generate templates
			

			#Template : scenario
			while count > 0 :
				if (count != nodeid) and (node_type(count) != "NaN") :
					#Rx nodes template
					t_rx = Template('node$rxnode:\n    entry rx_ofdm.py\n')
					#Rx nodes string	
					s_rx = s_rx + t_rx.safe_substitute(rxnode=count)
				count = count-1

			scenario_template = Template('desc CorteXlab Benchmark Tx Node : $txnode \ndurat 3\nnode$txnode:\n    entry tx_ofdm.py\n$rx_list')
			task_scenario = scenario_template.safe_substitute(txnode = nodeid , rx_list = s_rx)


			#Template : Task repertory
			task_directory_template = Template('benchmark_tx_node_$txnode')
			task_directory = task_directory_template.safe_substitute(txnode = nodeid)

			#Template : minus task create $file
			task_create_template = Template('minus task create benchmark_tx_node$txnode')
			task_create_command = task_create_template.safe_substitute(txnode = nodeid)
			
			#Template : minus task sumbit $file
			task_submit_template = Template('minus task submit benchmark_tx_node$txnode.task')
			task_submit_command = task_submit_template.safe_substitute(txnode = nodeid)


		#Create directories and execute Minus commands

			#create task directory
			if not os.path.exists(task_directory):
    				os.makedirs(task_directory)

			os.chdir(task_directory)
			########################################################################################################################
			## in ../Benchmark/benchmark_tx_node_X
			########################################################################################################################
			benchdir_1 = os.getcwd()
			#creer le scenario file desc
			task_create_scenario = Process(task_scenario)
			task_create_scenario.run()
			with open("scenario.desc", "w") as scen_file: 
				scen_file.write(task_scenario) 

			
			#execute "task create ..."
			task_create_process = Process(task_create_command)
			task_create_process.run()

			#create task directory
			if not os.path.exists("minus_std"):
    				os.makedirs("minus_std")

			os.chdir("minus_std")
			###########################################################################################################################################
			## in ../Benchmark/benchmark_tx_node_X/minus_std
			###########################################################################################################################################
			with open("minus_stderr.txt", "w") as err_file: 
				err_file.write(task_create_process.stderr) 
			with open("minus_stdout.txt", "w") as out_file: 
				out_file.write(task_create_process.stdout)
			os.chdir(benchdir_1)

			########################################################################################################################
			## in ../Benchmark/benchmark_tx_node_X
			########################################################################################################################
			# execute "task submit ..."
			task_submit_process = Process(task_submit_command)
			task_submit_process.run()
			

			# THIS PART IS CURRENTLY IN DEVELOPMENT
			# recuperer les resultats
			# p = Process("minus 
			# soit ca a fonctionne:
			sweeper.done(comb)
			# soit ca a pas fonctionne:
			# sweeper.skip(comb)

	

if __name__ == "__main__":
    engine = benchmark()
    engine.start()


