import random
import csv
random.seed

def generate_process(pcounter=10):
    """builds and array of random unlabelled integers"""
    process_metrics=[]

    for i in range (pcounter):

        process_metrics.append(random.randrange(0,101,1))
    
    print (process_metrics)
    return process_metrics

def persist_process(filename="process_output"):
    """persists the unlabled array to a csv file"""
    with open(filename + '.csv', 'a', newline='') as csvfile:
        write_csv = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        write_csv.writerow(generate_process())
