# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/vmargin
# catalog-date 2009-09-27 12:18:28 +0200
# catalog-license lppl
# catalog-version 2.5
Name:		texlive-vmargin
Version:	2.5
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides a macro to set various margins as well as dimensions
for header/footer and page dimensions. Most common paper sizes,
paper orientation, disabling of headers and footers, and two
sided printing are supported. The vmargin package does not rely
on other packages and was designed with speed and size in mind.
Its user interface might not be very fancy, but it's fast,
small, and gets the job done. If you are looking for something
more elaborate try the geometry package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
