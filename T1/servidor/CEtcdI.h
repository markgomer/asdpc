#ifndef CETCDIMPL_H_
#define CETCDIMPL_H_

#include "CEtcdS.h"
#include <string>
#include <map>


#if !defined (ACE_LACKS_PRAGMA_ONCE)
#pragma once
#endif

class CEtcd_impl : public virtual POA_CEtcd
{
public:
    
    CEtcd_impl(const std::string& account_id);
    ~CEtcd_impl () {}
    
    //virtual std::string id_() override;
    //virtual std::string id();
    virtual void put(std::string key, std::string val);
    virtual std::string get(std::string key);
    virtual void del(std::string key);
    virtual void shutdown(std::string password);

private:

    //std::string id_;
    std::map<std::string, std::string> table_;
};

#endif /* CETCDIMPL_H_  */
