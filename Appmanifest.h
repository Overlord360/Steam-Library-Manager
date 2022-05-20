#ifndef APPMANIFEST_H
    #define APPMANIFEST_H
    #include <string>
    #include <cstdlib>
    #include <iostream>
using namespace std;

class Appmanifest {
    public:
    //constructors
    Appmanifest();
    Appmanifest(const int);

    //destructors
    ~Appmanifest();
    
    //getters
    int getID() const;

    //setters
    void setID(const int);

    private:
    int ID;


};
ostream& operator <<(ostream&, const Appmanifest&);

#endif