#ifndef SLM_MANILIST
    #define SLM_MANILIST
    #include "ManifestList.h"
#endif
#ifndef SLM_APPMANIFEST
    #define SLM_APPMANIFEST
    #include "Appmanifest.h"
#endif
#ifndef SLM_STD
    #define SLM_STD
    #include <iostream>
    #include <iterator>
    #include <list>
#endif

ManifestList::ManifestList(){
    DT emptyManifest;
    manifests.push_front(emptyManifest);
}
ManifestList::ManifestList(DT dataIn){
    manifests.push_front(dataIn);
}

void ManifestList::push(DT dataIn){
    manifests.push_back(dataIn);
}

DT ManifestList::pop(){
    DT mani = manifests.back();
    manifests.pop_back();
    return mani;
}
int ManifestList::size(){
    return manifests.size();
}

ManifestList::~ManifestList(){
    manifests.clear();
    delete &manifests; //this may be fucked
}    

ostream& operator<<(ostream& stream, ManifestList& object){
    stream << "size(" << object.size() << ")";
    return stream;
}
