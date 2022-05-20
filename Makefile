CC=g++
CFLAGS=-c -Wall
LDFLAGS=
SOURCES= SteamLibraryManager.cpp ManifestList.cpp Appmanifest.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=SteamLibraryManager

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

%.o : %.cpp
	$(CC) $(CFLAGS) -c $<

clean:
	rm -rf *.o core
