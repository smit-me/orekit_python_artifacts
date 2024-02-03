import orekit
vm = orekit.initVM()
print ('Java version:',vm.java_version)
print ('Orekit version:', orekit.VERSION)

from orekit.pyhelpers import download_orekit_data_curdir
#download_orekit_data_curdir()

File orekitData = new File("/path/to/the/folder/orekit-data");
DataProvidersManager manager = DataContext.getDefault().getDataProvidersManager();
manager.addProvider(new DirectoryCrawler(orekitData));


from org.orekit.utils import Constants
