Summary:	Multitech Intelligent Serial Internal (ISI) firmware
Name:		isicom-firmware
Version:	3.09
Release:	2
License:	Distributable
Group:		System/Kernel and hardware
URL:		http://www.multitech.com/
Source0:	ftp://ftp.multitech.com/isi-cards/linux/l309_22x_24x.tar
BuildArch:	noarch

%description
The isicom package contains the firmware for Multi-Tech Systems Intelligent
Serial Interface(TM) (ISI) cards.
Multi-Tech ISI multiport serial cards provide additional serial
ports for remote access servers, multi-user hosts and PCs.

%prep
%setup -qcn %{name}-%{version}

%build

%install
install -d %{buildroot}/lib/firmware/
install -m644 *.bin %{buildroot}/lib/firmware/ 

%files
/lib/firmware/*.bin
