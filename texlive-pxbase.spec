Name:		texlive-pxbase
Version:	1.1b
Release:	2
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
%{_texmfdistdir}/tex/platex/pxbase
%doc %{_texmfdistdir}/doc/platex/pxbase

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
