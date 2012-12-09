# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/vmargin
# catalog-date 2009-09-27 12:18:28 +0200
# catalog-license lppl
# catalog-version 2.5
Name:		texlive-vmargin
Version:	2.5
Release:	2
Summary:	Set various page dimensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vmargin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vmargin.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5-2
+ Revision: 757473
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.5-1
+ Revision: 719892
- texlive-vmargin
- texlive-vmargin
- texlive-vmargin

