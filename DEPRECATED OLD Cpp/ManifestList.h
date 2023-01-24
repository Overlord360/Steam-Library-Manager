#ifndef SLM_STD
    #define SLM_STD
    #include <iostream>
    #include <iterator>
    #include <list>
#endif
#ifndef SLM_APPMANIFEST
#define SLM_APPMANIFEST
    #include "Appmanifest.h"
#endif


using namespace std;
typedef Appmanifest DT;

class ManifestList{
    public:
        //constructors
        ManifestList();
        ManifestList(DT dataIn);

        void push(DT dataIn);
        DT pop();
        int size();

        ~ManifestList();
    private:
        //stuff
        list<DT> manifests;
};

ostream& operator<<(ostream& stream, ManifestList& object);