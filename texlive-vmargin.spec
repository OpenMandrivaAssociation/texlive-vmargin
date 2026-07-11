%global tl_name vmargin
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	Set various page dimensions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vmargin
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a macro to set various margins as well as dimensions for
header/footer and page dimensions. Most common paper sizes, paper
orientation, disabling of headers and footers, and two sided printing
are supported. The vmargin package does not rely on other packages and
was designed with speed and size in mind. Its user interface might not
be very fancy, but it's fast, small, and gets the job done. If you are
looking for something more elaborate try the geometry package.

