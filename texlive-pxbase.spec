# revision 28516
# category Package
# catalog-ctan /language/japanese/pxbase
# catalog-date 2012-12-12 11:03:41 +0100
# catalog-license other-free
# catalog-version 0.5
Name:		texlive-pxbase
Version:	0.5
Release:	9
Summary:	Tools for use with (u)pLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/pxbase
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxbase.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxbase.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive pxbase package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/platex/pxbase/ifuptex.sty
%{_texmfdistdir}/tex/platex/pxbase/pxbabel.sty
%{_texmfdistdir}/tex/platex/pxbase/pxbase.def
%{_texmfdistdir}/tex/platex/pxbase/pxbase.sty
%{_texmfdistdir}/tex/platex/pxbase/pxbasenc.def
%{_texmfdistdir}/tex/platex/pxbase/pxbsjc.def
%{_texmfdistdir}/tex/platex/pxbase/pxjsfenc.def
%{_texmfdistdir}/tex/platex/pxbase/upkcat.sty
%doc %{_texmfdistdir}/doc/platex/pxbase/LICENSE
%doc %{_texmfdistdir}/doc/platex/pxbase/README
%doc %{_texmfdistdir}/doc/platex/pxbase/README-pxbabel
%doc %{_texmfdistdir}/doc/platex/pxbase/README-pxcjkcat

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
