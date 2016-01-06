exe = "myprog"
#staticlib = "libmylib.a"

# "gnu" is a predefined toolchain
toolchain = "gnu"

# optional
link_pool_depth = 1

# reuired
includes = {
    "gnu" : [ "-I." ]
  , "clang" : [ "-I." ]
    }

# reuired
defines = {
    "gnu" : [ "-DEXAMPLE=1" ]
  , "clang" : [ "-DEXAMPLE=1" ]
    }

# reuired
cflags = {
    "gnu" : [ "-O2", "-g" ]
  , "clang" : [ "-O2", "-g" ]
    }

# reuired
cxxflags = {
    "gnu" : [ "-O2", "-g" ]
  , "clang" : [ "-O2", "-g", "-fsanitize=address" ]
    }

# reuired
ldflags = {
    "gnu" : [ ]
  , "clang" : [ "-fsanitize=address" ]
    }

# optionsl
cxx_files = [ "main.cc" ]
c_files = [ "add.c" ]

# You can register your own toolchain through register_toolchain function
def register_toolchain(ninja):
    pass

    #ninja.rule('clangcxx', description='CXX $out',
    #    command='$clangcxx -MMD -MF $out.d $clangdefines $clangincludes $clangcxxflags -c $in -o $out',
    #    depfile='$out.d', deps='gcc')
    #ninja.rule('clangcc', description='CC $out',
    #    command='$clangcc -MMD -MF $out.d $clangdefines $clangincludes $clangcflags -c $in -o $out',
    #    depfile='$out.d', deps='gcc')
    #ninja.rule('clanglink', description='LINK $out', pool='link_pool',
    #    command='$clangld $clangldflags -o $out $in $libs')
    #ninja.rule('clangar', description='AR $out', pool='link_pool',
    #    command='$clangar rsc $out $in')
    #ninja.rule('clangstamp', description='STAMP $out', command='touch $out')
    #ninja.newline()

    #ninja.variable('clangcxx', 'clang++')
    #ninja.variable('clangcc', 'clang')
    #ninja.variable('clangld', 'clang++')
    #ninja.variable('clangar', 'ar')
    #ninja.newline()


