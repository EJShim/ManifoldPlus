import vtk


if __name__ == "__main__":

    sphereSource = vtk.vtkSphereSource()
    # sphereSource.SetPhiResolution(100)
    # sphereSource.SetThetaResolution(100)
    sphereSource.Update()


    # reader = vtk.vtkSTLReader()
    # reader.SetFileName("./sampleData/maxilary.stl")
    # reader.Update()

    # reader = vtk.vtkXMLPolyDataReader()
    # reader.SetFileName("./sampleData/sample1.vtp")
    # reader.Update()
    # reader.GetOutput()
    

    data = sphereSource.GetOutput()

    objWriter = vtk.vtkOBJWriter()
    objWriter.SetInputData(data)
    objWriter.SetFileName("./sampleData/sphere_low.obj")
    objWriter.Update()
