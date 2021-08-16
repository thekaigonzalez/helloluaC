#include <lua5.3/lua.h>
#include <lua5.3/lualib.h>
#include <lua5.3/lauxlib.h>

int main()
{
    lua_State* L = luaL_newstate();
    luaL_openlibs(L);
    luaL_dofile(L, "./hello.lua");
}