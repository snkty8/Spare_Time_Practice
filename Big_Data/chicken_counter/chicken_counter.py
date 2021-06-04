from mrjob.job import MRJob
class Chicken_count(MRJob):
   def mapper(self, _, line):
       for word in line.split():
           if word.lower() == "chicken":
               yield "chicken", 1

   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Chicken_count.run()


