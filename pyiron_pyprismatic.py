from pyiron.base.job.template import TemplateJob
import pyprismatic as pr
from pyprismatic.fileio import readMRC
import matplotlib.pyplot as plt

class PrismaticJob(TemplateJob):
    def __init__(self, project, job_name):
        super(PrismaticJob, self).__init__(project, job_name) 
        self.input['filenameAtoms'] = None
        self.input['filenameOutput'] = 'output.mrc'
        self.input['algorithm'] = 'multislice' 
        
    def run_static(self):
        meta = Metadata(filenameAtoms=self.input['filenameAtoms'],
                 filenameOutput=self.input['filenameOutput'])
        meta.algorithm = self.input['algorithm']
        meta.go()
        print ('OK 1')
        with self.project_hdf5.open("output/generic") as h5out: 
            result = readMRC(self.input['filenameOutput'])
            print ('OK 2')
            h5out["result"] = result 
            print ('OK 3')
        self.status.finished = True

    def plotting():
        result = self["output/generic/result"]
        plt.imshow(np.squeeze(np.sum(result, axis=2)))

    @property
    def filenameAtoms(self):
        return self.input['filenameAtoms']
    @filenameAtoms.setter
    def filenameAtoms(self, filenameAtoms):
        self.input['filenameAtoms'] = filenameAtoms
        
    @property
    def filenameOutput(self):
        return self.input['filenameOutput']
    @filenameOutput.setter
    def filenameOutput(self,filenameOutput):
        self.input['filenameOutput'] = filenameOutput

    @property
    def algorithm(self):
        return self.input['algorithm']
    @algorithm.setter
    def algorithm(self, algorithm):
        self.input['algorithm'] = algorithm
