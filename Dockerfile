FROM ubuntu:latest

RUN apt-get update

# Timezone gets stuck for whatever reason
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get install -y build-essential \ 
		       git-core \ 
		       m4 \  
                       scons \ 
		       zlib1g \ 
                       zlib1g-dev \ 
                       libprotobuf-dev \ 
                       protobuf-compiler \ 
		       fish \
		       tmux \
		       neovim \
                       libprotoc-dev \ 
		       libgoogle-perftools-dev \ 
		       swig \ 
 		       python3-dev \ 
		       python3-six \
		       python-is-python3 \
		       libboost-all-dev \
		       pkg-config

RUN apt-get clean

WORKDIR /gem5-dev

# Build X86
#RUN scons build/X86/gem5.opt
