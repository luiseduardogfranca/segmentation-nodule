import pydicom
import os
import numpy as np
from matplotlib import pyplot, cm

def getListFile(path):

    listFilesDCM = []

    for dirName, subdirList, fileList in os.walk(path):
        for filename in fileList:
            if (".dcm" in filename.lower()):
                listFilesDCM.append(os.path.join(dirName, filename))

    return listFilesDCM


#get dimensions of the DICOM file
def getFileDimensions(fileDCM, listFilesDCM):
    return (int(fileDCM.Rows), int(fileDCM.Columns), len(listFilesDCM))

#get spacing values of the DICOM file
def getValueSpacing(fileDCM):
    return (float(fileDCM.PixelSpacing[0]), float(fileDCM.PixelSpacing[1]), float(fileDCM.SliceThickness))


listFilesDCM = getListFile("/home/eduardo/Documentos/Projeto/Python and DICOM/patient/1/1")
fileDCM = pydicom.read_file(listFilesDCM[0])
print(fileDCM.pixel_array)
ConstPixelDims = getFileDimensions(fileDCM, listFilesDCM)
ConstPixelSpacing = getValueSpacing(fileDCM)

# calcule axes for this array:

# x = np.arange(0.0, (ConstPixelDims[0] + 1) * ConstPixelSpacing[0], ConstPixelSpacing[0])
#
# y = np.arange(0.0, (ConstPixelDims[1] + 1) * ConstPixelSpacing[1], ConstPixelSpacing[1])
#
# z = np.arange(0.0, (ConstPixelDims[2] + 1) * ConstPixelSpacing[2], ConstPixelSpacing[2])
#
# # new array
# arrayDicom = np.zeros(ConstPixelDims, dtype=fileDCM.pixel_array.dtype)

# # for filename in listFilesDCM:
# #
# #     ds = pydicom.read_file(filename)
# #
# #     #store imaga data
# #     arrayDicom[:, :, listFilesDCM.index(filename)] = ds.pixel_array
# #     print(ds.pixel_array)
#
# pyplot.figure(dpi=300)
# pyplot.axes().set_aspect('equal', 'datalim')
# pyplot.set_cmap(pyplot.gray())
# pyplot.pcolormesh(x,y,np.flipud(arrayDicom[:, :, 80]))
# # print(arrayDicom[1,1,:])

#code emerson
# import xmltodict
# import json
#
# with open("069.xml", 'r') as f:
#     xmlString = f.read()
#
# jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
#
# obj = json.loads(jsonString)
#
# def doImageMasked(image, mask):
#     """image = image pixels array
#         mask = mask coords array
#     """
#
#     plt.figure(figsize=(12, 12))
#     plt.imshow(np.zeros(image.shape), cmap='Greys')
#     plt.imshow(image, cmap=plt.cm.gray)
#     return plt.gca().add_patch(matplotlib.patches.Polygon(mask, True, ec='r', fc='none'))
#
# def getMaskCoords(zPosition):
#     """
#     zPosition= must be a int or float of slice position
#     """
#     zPosition = str(zPosition)
#
#     for sess in sessions:
#         try:
#             for nodules in sess['unblindedReadNodule']:
#                 for roi in nodules['roi']:
#                     if roi['imageZposition'] == zPosition:
#                         return [[i[j] for j in i.keys()] for i in roi['edgeMap']]
#         except:
#             pass
