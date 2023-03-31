Name:		texlive-vmargin
Version:	15878
Release:	2
Summary:	Set various page dimensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vmargin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a macro to set various margins as well as dimensions
for header/footer and page dimensions. Most common paper sizes,
paper orientation, disabling of headers and footers, and two
sided printing are supported. The vmargin package does not rely
on other packages and was designed with speed and size in mind.
Its user interface might not be very fancy, but it's fast,
small, and gets the job done. If you are looking for something
more elaborate try the geometry package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vmargin/vmargin.sty
%doc %{_texmfdistdir}/doc/latex/vmargin/vmargin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/vmargin/Makefile
%doc %{_texmfdistdir}/source/latex/vmargin/vmargin.drv
%doc %{_texmfdistdir}/source/latex/vmargin/vmargin.dtx
%doc %{_texmfdistdir}/source/latex/vmargin/vmargin.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
