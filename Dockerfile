FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y build-essential \ 
		       git-core \ 
		       m4 \  
                       scons \ 
		       zlib1g \ 
                       zlib1g-dev \ 
                       libprotobuf-dev \ 
                       protobuf-compiler \ 
                       libprotoc-dev libgoogle-perftools-dev swig python-dev python

RUN apt-get clean

# Build X86
RUN scons build/X86/gem5.opt
