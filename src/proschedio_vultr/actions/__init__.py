from .instance import Instance
from .block_storage import BlockStorage
from .database import Database
from .account import Account
from .applications import Applications
from .backups import Backups
from .bare_metal import BareMetal
from .billings import Billing
from .cdns import CDNs
from .container_registry import ContainerRegistry
from .dns import DNS
from .firewall import Firewall
from .inference import Inference
from .iso import Iso
from .kubernetes import Kubernetes
from .load_balancers import LoadBalancers
from .marketplace import Marketplace
from .object_storage import ObjectStorage
from .operating_systems import OperatingSystems
from .plans import Plans
from .plans_metal import PlansMetal
from .regions import Regions
from .reserved_ips import ReservedIPs
from .snapshots import Snapshots
from .ssh_keys import SSHKeys
from .startup_script import StartupScript
from .subaccounts import Subaccounts
from .users import Users
from .vfs import VFS
from .vpc2 import VPC2
from .vpcs import VPCs


class Action:
    
    @staticmethod
    def instance() -> Instance:
        return Instance()
    
    @staticmethod
    def block_storage() -> BlockStorage:
        return BlockStorage()
    
    @staticmethod
    def database() -> type[Database]:
        return Database

    @staticmethod
    def account() -> Account:
        return Account()

    @staticmethod
    def applications() -> Applications:
        return Applications()

    @staticmethod
    def backups() -> Backups:
        return Backups()

    @staticmethod
    def bare_metal() -> BareMetal:
        return BareMetal()

    @staticmethod
    def billings() -> Billing:
        return Billing()

    @staticmethod
    def cdns() -> CDNs:
        return CDNs()

    @staticmethod
    def container_registry() -> ContainerRegistry:
        return ContainerRegistry()

    @staticmethod
    def dns() -> DNS:
        return DNS()

    @staticmethod
    def firewall() -> Firewall:
        return Firewall()

    @staticmethod
    def inference() -> Inference:
        return Inference()

    @staticmethod
    def iso() -> Iso:
        return Iso()

    @staticmethod
    def kubernetes() -> Kubernetes:
        return Kubernetes()

    @staticmethod
    def load_balancers() -> LoadBalancers:
        return LoadBalancers()

    @staticmethod
    def marketplace() -> Marketplace:
        return Marketplace()

    @staticmethod
    def object_storage() -> ObjectStorage:
        return ObjectStorage()

    @staticmethod
    def operating_systems() -> OperatingSystems:
        return OperatingSystems()

    @staticmethod
    def plans() -> Plans:
        return Plans()

    @staticmethod
    def plans_metal() -> PlansMetal:
        return PlansMetal()

    @staticmethod
    def regions() -> Regions:
        return Regions()

    @staticmethod
    def reserved_ips() -> ReservedIPs:
        return ReservedIPs()

    @staticmethod
    def snapshots() -> Snapshots:
        return Snapshots()

    @staticmethod
    def ssh_keys() -> SSHKeys:
        return SSHKeys()

    @staticmethod
    def startup_script() -> StartupScript:
        return StartupScript()

    @staticmethod
    def subaccounts() -> Subaccounts:
        return Subaccounts()

    @staticmethod
    def users() -> Users:
        return Users()

    @staticmethod
    def vfs() -> VFS:
        return VFS()

    @staticmethod
    def vpc2() -> VPC2:
        return VPC2()

    @staticmethod
    def vpcs() -> VPCs:
        return VPCs()