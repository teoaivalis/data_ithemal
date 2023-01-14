import torch
import torchvision


file1 = open("/home/delluser/Documents/ithemal/bhive/timing-harness/hexcodes_hsw_1txt", "r")
file2 = open("/home/delluser/Documents/ithemal/bhive/timing-harness/throughput1.txt", "r")
file3 = open("/home/delluser/Documents/ithemal/bhive/timing-harness/output_hsw_1.txt", "r")

content1 = file1.readlines()
content2 = file.2readlines()
content3 = hsw
content4 = file3.readlines()

for i in range(171850):
	x = torch.tensor([content1[i], content2[i], content3, content4[i])
	torch.save(x, 'tensor.pt')

