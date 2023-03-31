Name:		texlive-utf8add
Version:	61074
Release:	2
Summary:	Additional support for UTF-8 encoded LaTeX input
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/utf8add
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utf8add.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utf8add.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle contains the LaTeX packages utf8add.sty and
utf8hax.sty. The utf8add package provides additional support
for the use of UTF-8 encoded input. This is intended for making
LaTeX input more readable. The utf8hax package is using UTF-8
characters for easier access to math in LaTeX, however making
the LaTeX input less readable.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/utf8add
%doc %{_texmfdistdir}/doc/latex/utf8add

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
