CXX = gcc
CXXFLAGS = -Wall -g

# ****************************************************
# Targets needed to bring the executable up to date

server:
	$(CXX) $(CXXFLAGS) -o server server.c

client:
	$(CXX) $(CXXFLAGS) -o client client.c

clean: 
	rm -f server client
	echo "Clean done"
