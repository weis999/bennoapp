FROM ubuntu:18.04                                                                                         
                                                                                                          
# Maintainer of Dockerfile                                                                                
MAINTAINER Weis Mateen <weis.mateen@sue.nl>                                                               
                                                                                                          
# Packages defined                                                                                        
ENV DEBIAN_FRONTEND="noninteractive" \                                                                    
    TERM="xterm" \                                                                                        
    APTLIST="apt-utils coreutils python3 python3-pip python3-dev curl" \                                  
    REFRESHED_AT='2020-03-10'                                                                             
                                                                                                          
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup &&\                                       
    echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \                            
    apt-get -q update && \                                                                                
    apt-get -qy dist-upgrade && \                                                                         
    apt-get install -qy $APTLIST && \                                                                     
    \                                                                                                     
    # Cleanup                                                                                             
    apt-get -y autoremove && \                                                                            
    apt-get -y clean && \                                                                                 
    rm -rf /var/lib/apt/lists/* && \                                                                      
    rm -rf /tmp/*                                                                                         
                                                                                                          
#Copy                                                                                                     
COPY ./flask /flask                                                                                       
                                                                                                          
#Flask                                                                                                    
RUN pip3 install -r /flask/requirements.txt                                                               
CMD python3 /flask/app.py 
