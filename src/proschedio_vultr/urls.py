from typing import Final

from .request import Url

URL_BASE: Final[str] = "https://api.vultr.com/v2/"

URL_ACCOUNT: Final[Url] = Url(URL_BASE).uri("account")
"""
### Request Methods
- `GET`: Get your Vultr account, permission, and billing information.

### Response Schema
- `GET`:

```js
{
    "account": {
	    b
	}
}
```
"""

URL_ACCOUNT_BANDWIDTH: Final[Url] = Url(URL_BASE).uri("account/bandwidth")
"""
### Request Methods
- `GET`: Get your Vultr account bandwidth information.
"""

URL_ACCOUNT_BGP: Final[Url] = Url(URL_BASE).uri("account/bgp")
"""
### Request Methods
- `GET`: Get your Vultr account BGP information.
"""

URL_APPLICATIONS: Final[Url] = Url(URL_BASE).uri("applications")
"""
### Request Methods
- `GET`: List all available Applications.

### Query parameters
- `per_page` - (optional) Number of items requested per page. Default is 100.
- `cursor` - (optional) Cursor for paging.
- `type` - (optional) Filter by type, `marketplace` or `one-click`.
"""

URL_BACKUPS: Final[Url] = Url(URL_BASE).uri("backups")
"""
### Request Methods
- `GET`: Get information about Backups in your account.

### Query parameters
- `GET`:
    - `instance_id` - Filter the backups list by Instance id.
    - `per_page` - Number of items requested per page. Default is 100 and max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.
"""

URL_BACKUPS_ID: Final[Url] = Url(URL_BASE).uri("backups/{backup-id}")
"""
### Request Methods
- `GET`: Get the information for the Backup.

### Path parameters
- `backup_id` - The Backup id.
"""

URL_BARE_METAL: Final[Url] = Url(URL_BASE).uri("bare-metals")
"""
### Request Methods
- `GET`: List all Bare Metal instances in your account.
- `POST`: Create a new Bare Metal instance in a `region` with the desired `plan`. Choose one of the following to deploy the instance:
    - `os_id`
    - `snapshot_id`
    - `app_id`
    - `image_id`

Supply other attributes as desired.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.

### Request Body Schema
- `POST`:

```js
{
    "region": String, // The [Region id](#operation/list-regions) to create the instance.
    "plan": String, // The [Bare Metal plan id](#operation/list-metal-plans) to use for this instance.
    "script_id": Optional<String>, // The [Startup Script id](#operation/list-startup-scripts) to use for this instance.
    "enable_ipv6": Optional<Boolean>, // Enable IPv6. * true
    "sshkey_id": Optional<Array<Strings>>, // The [SSH Key id](#operation/list-ssh-keys) to install on this instance.
    "user_data": Optional<String>, // The user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) for this Instance.
    "label": Optional<String>, // The user-supplied label.
    "activation_email": Optional<Boolean>, // Notify by email after deployment. * true * false (default)
    "hostname": Optional<String>, // The user-supplied hostname to use when deploying this instance.
    "reserved_ipv4": Optional<String>, // The [Reserved IP id](#operation/list-reserved-ips) for this instance.
    "os_id": Optional<Integer>, // If supplied, deploy the instance using this [Operating System id](#operation/list-os).
    "snapshot_id": Optional<String>, // If supplied, deploy the instance using this [Snapshot ID](#operation/list-snapshots).
    "app_id": Optional<Integer>, // If supplied, deploy the instance using this [Application id](#operation/list-applications).
    "image_id": Optional<String>, // If supplied, deploy the instance using this [Application image_id](#operation/list-applications).
    "persistent_pxe": Optional<Boolean>, // Enable persistent PXE. * true * false (default)
    "attach_vpc2": Optional<Array<Strings>>, // An array of [VPC IDs](#operation/list-vpc2) to attach to this Bare Metal Instance. This parameter takes precedence over `enable_vpc2`.  Please choose one parameter.
    "detach_vpc2": Optional<Array<Strings>>, // An array of [VPC IDs](#operation/list-vpc2) to detach from this Bare Metal Instance. This parameter takes precedence over `enable_vpc2`.
    "enable_vpc2": Optional<Boolean>, // If `true`, VPC 2.0 support will be added to the new server.
    "tags": Optional<Array<Strings>>, // Tags to apply to the instance.
    "user_scheme": Optional<String>, // Linux-only: The user scheme used for logging into this instance. * root * limited
    "mdisk_mode": Optional<String>, // The RAID configuration used for the disks on this instance. * raid1 * jbod * none (default)
    "app_variables": Optional<Object> // The [app variable inputs](#operation/list-marketplace-app-variables) for configuring the marketplace app (name/value pairs).
}
```
"""

URL_BARE_METAL_ID: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}")
"""
### Request Methods
- `GET`: Get information for a Bare Metal instance.
- `PATCH`: Update a Bare Metal instance. All attributes are optional. If not set, the attributes will retain their original values.
- `DELETE`: Delete a Bare Metal instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `PATCH`:

```js
{
    "user_data": Optional<String>, // The user-supplied, base64 encoded user data to attach to this instance.
    "label": Optional<String>, // The user-supplied label.
    "tag": Optional<String>, // Deprecated: Use tags instead. The user-supplied tag.
    "os_id": Optional<String>, // If supplied, reinstall the instance using this [Operating System id](#operation/list-os).
    "app_id": Optional<String>, // If supplied, reinstall the instance using this [Application id](#operation/list-applications).
    "image_id": Optional<String>, // If supplied, reinstall the instance using this [Application image_id](#operation/list-applications).
    "enable_ipv6": Optional<Boolean>, // Enable IPv6. * true
    "attach_vpc2": Optional<Array<String>>, // An array of [VPC IDs](#operation/list-vpc2) to attach to this Bare Metal Instance. This parameter takes precedence over enable_vpc2. Please choose one parameter.
    "detach_vpc2": Optional<Array<String>>, // An array of [VPC IDs](#operation/list-vpc2) to detach from this Bare Metal Instance. This parameter takes precedence over enable_vpc2.
    "enable_vpc2": Optional<Boolean>, // If true, VPC 2.0 support will be added to the new server. This parameter attaches a single VPC 2.0 netowrk. When no VPC 2.0 network exists in the region, it will be automatically created. If there are multiple VPC 2.0 networks in the instance's region, use attach_vpc2 instead to specify a VPC 2.0 network.
    "tags": Optional<Array<String>>, // Tags to apply to the instance.
    "user_scheme": Optional<String>, // Linux-only: The user scheme used for logging into this instance. The instance must be reinstalled for this change to take effect. * root * limited
    "mdisk_mode": Optional<String> // The RAID configuration used for the disks on this instance. The instance must be reinstalled for this change to take effect. * raid1 * jbod * none(default)
}
```
"""

URL_BARE_METAL_IPV4: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/ipv4")
"""
### Request Methods
- `GET`: Get the IPv4 information for the Bare Metal instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_IPV6: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/ipv6")
"""
### Request Methods
- `GET`: Get the IPv6 information for the Bare Metal instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_IPV4_REVERSE: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/ipv4/reverse")
"""
### Request Methods
- `POST`: Create a reverse IPv4 entry for a Bare Metal Instance. The `ip` and `reverse` attributes are required.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:

```js
{
    "ip": String, // The IPv4 address.
    "reverse": String // The IPv4 reverse entry.
}
```
"""

URL_BARE_METAL_IPV6_REVERSE: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/ipv6/reverse")
"""
### Request Methods
- `POST`: Create a reverse IPv6 entry for a Bare Metal Instance. The `ip` and `reverse` attributes are required. IP address must be in full, expanded format.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:

```js
{
    "ip": String, // The IPv6 address in full, expanded format.
    "reverse": String // The IPv6 reverse entry.
}
```
"""

URL_BARE_METAL_IPV4_REVERSE_DEFAULT: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/ipv4/reverse/default")
"""
### Request Methods
- `POST`: Set a reverse DNS entry for an IPv4 address.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:

```js
{
    "ip": String // The IPv4 address.
}
```
"""

URL_BARE_METAL_IPV6_REVERSE_IPV6: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/ipv6/reverse/{ipv6}")
"""
### Request Methods
- `DELETE`: Delete the reverse IPv6 for a Bare metal instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
- `ipv6` - The IPv6 address.
"""

URL_BARE_METAL_START: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/start")
"""
### Request Methods
- `POST`: Start the Bare Metal instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_REBOOT: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/reboot")
"""
### Request Methods
- `POST`: Reboot the Bare Metal instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_REINSTALL: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/reinstall")
"""
### Request Methods
- `POST`: Reinstall the Bare Metal instance using an optional `hostname`.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:

```js
{
    "hostname": String // The hostname to use when reinstalling this bare metal server.
}
```
"""

URL_BARE_METAL_HALT: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/halt")
"""
### Request Methods
- `POST`: Halt the Bare Metal instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_BANDWIDTH: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/bandwidth")
"""
### Request Methods
- `GET`: Get bandwidth information for the Bare Metal instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

The `bandwidth` object in a successful response contains objects representing a day in the month. The date is denoted by the nested object keys. Days begin and end in the UTC timezone. Bandwidth utilization data contained within the date object is refreshed periodically. We do not recommend using this endpoint to gather real-time metrics.
"""

URL_BARE_METALS_HALT: Final[Url] = Url(URL_BASE).uri("bare-metals/halt")
"""
### Request Methods
- `POST`: Halt Bare Metals.

### Request Body Schema
- `POST`:

```js
{
    "baremetal_ids": Array<String> // Array of Bare Metal instance ids to halt.
}
```
"""

URL_BARE_METALS_REBOOT: Final[Url] = Url(URL_BASE).uri("bare-metals/reboot")
"""
### Request Methods
- `POST`: Reboot Bare Metals.

### Request Body Schema
- `POST`:

```js
{
    "baremetal_ids": Array<String> // Array of Bare Metal instance ids to reboot.
}
```
"""

URL_BARE_METALS_START: Final[Url] = Url(URL_BASE).uri("bare-metals/start")
"""
### Request Methods
- `POST`: Start Bare Metals.

### Request Body Schema
- `POST`:

```js
{
    "baremetal_ids": Array<String> // Array of Bare Metal instance ids to start.
}
```
"""

URL_BARE_METALS_USER_DATA: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/user-data")
"""
### Request Methods
- `GET`: Get the user-supplied, base64 encoded [user data] for a Bare Metal.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METALS_ID_AVAILABLE_UPGRADES: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/upgrades")
"""
### Request Methods
- `GET`: Get available upgrades for a Bare Metal.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Query parameters
- `type` - Filter upgrade by type:
    - all (applications, plans)
    - applications
    - os
"""

URL_BARE_METALS_ID_VNC: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/vnc")
"""
### Request Methods
- `GET`: Get the VNC URL for a Bare Metal.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METALS_ATTACH_VPC_TO_INSTANCE: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/vpcs/attach")
"""
### Request Methods
- `POST`: Attach a VPC Network to a Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpcs) to attach.
}
```
"""

URL_BARE_METALS_DETACH_VPC_FROM_INSTANCE: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/vpcs/detach")
"""
### Request Methods
- `POST`: Detach a VPC Network from an Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpcs) to detach.
}
```
"""

URL_BARE_METALS_VPCS: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/vpcs")
"""
### Request Methods
- `GET`: List the VPC networks for a Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METALS_ATTACH_VPC2_TO_INSTANCE: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/vpc2/attach")
"""
### Request Methods
- `POST`: Attach a VPC 2.0 Network to a Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:

```js
{
    "vpc_id": Optional<String>, // The [VPC ID](#operation/list-vpc2) to attach.
    "ip_address": Optional<String> // The IP address to use for this instance on the attached VPC 2.0 network.
}
```
"""

URL_BARE_METALS_DETACH_VPC2_FROM_INSTANCE: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/vpc2/detach")
"""
### Request Methods
- `POST`: Detach a VPC 2.0 Network from an Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpc2) to detach.
}
```
"""

URL_BARE_METALS_VPCS2: Final[Url] = Url(URL_BASE).uri("bare-metals/{baremetal-id}/vpc2")
"""
### Request Methods
- `GET`: List the VPC 2.0 networks for a Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

"""

URL_BILLING_LIST_HISTORY: Final[Url] = Url(URL_BASE).uri("billing/history")
"""
### Request Methods
- `GET`: Retrieve billing history entries.

### Query Parameters
- `per_page`: Number of items requested per page. Default is 100, maximum is 500.
- `cursor`: Cursor for pagination.
"""

URL_BILLING_INVOICES: Final[Url] = Url(URL_BASE).uri("billing/invoices")
"""
### Request Methods
- `GET`: Retrieve a list of all invoices on the account.

### Query Parameters
- `per_page`: Number of items requested per page. Default is 100, maximum is 500.
- `cursor`: Cursor for pagination.
"""

URL_BILLING_INVOICE_ID: Final[Url] = Url(URL_BASE).uri("billing/invoices/{invoice-id}")
"""
### Request Methods
- `GET`: Retrieve a specific invoice by ID.

### Path Parameters
- `invoice-id`: The ID of the invoice to retrieve.
"""

URL_BILLING_INVOICE_ID_ITEMS: Final[Url] = Url(URL_BASE).uri("billing/invoices/{invoice-id}/items")
"""
### Request Methods
- `GET`: Retrieve line items for a specific invoice.

### Path Parameters
- `invoice-id`: The ID of the invoice.

### Query Parameters
- `per_page`: Number of items requested per page. Default is 100, maximum is 500.
- `cursor`: Cursor for pagination.
"""

URL_BILLING_LIST_PENDING_CHARGES: Final[Url] = Url(URL_BASE).uri("billing/pending-charges")
"""
### Request Methods
- `GET`: Retrieve all pending charges for the account.
"""

URL_BLOCK_STORAGE: Final[Url] = Url(URL_BASE).uri("blocks")
"""
### Request Methods
- `GET`: List all Block Storage in your account.
- `POST`: Create new Block Storage in a `region` with a size of `size_gb`.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.

### Request Body Schema
- `POST`:

```js
{
    "region": String, // The [Region id](#operation/list-regions) where the Block Storage will be created.
    "size_gb": Integer, // Size in GB may range between 10 and 40000, depending on the block_type.
    "label": Optional<String>, // The user-supplied label.
    "block_type": Optional<String> // An optional parameter, that determines the type of block storage volume.
    // high_perf from 10GB to 10,000GB
    // storage_opt from 40GB to 40,000GB
}
```
"""

URL_BLOCK_STORAGE_ID: Final[Url] = Url(URL_BASE).uri("blocks/{block-id}")
"""
### Request Methods
- `GET`: Get information for Block Storage.
- `PATCH`: Update information for Block Storage.
- `DELETE`: Delete Block Storage.

### Path parameters
- `block-id` - The Block Storage id.

### Request Body Schema
- `PATCH`:

```js
{
    "label": Optional<String>, // The user-supplied label.
    "size_gb": Optional<Integer> // The new size of the block storage volume in GB. Must be >= current size.
}
```
"""

URL_BLOCK_STORAGE_ATTACH: Final[Url] = Url(URL_BASE).uri("blocks/{block-id}/attach")
"""
### Request Methods
- `POST`: Attach Block Storage to Instance.

### Path parameters
- `block-id` - The Block Storage id.

### Request Body Schema
- `POST`:

```js
{
    "instance_id": String, // The [Instance id](#operation/list-instances) to attach.
    "live": Optional<Boolean> // Attach without restarting the Instance.
    // true: Attach live
    // false: Restart and attach (default)
}
```
"""

URL_BLOCK_STORAGE_DETACH: Final[Url] = Url(URL_BASE).uri("blocks/{block-id}/detach")
"""
### Request Methods
- `POST`: Detach Block Storage.

### Path parameters
- `block-id` - The Block Storage id.

### Request Body Schema
- `POST`:

```js
{
    "live": Optional<Boolean> // Detach without restarting the Instance.
}
```

|Value|Description|
|----|----|
|true|Detach live, do not restart the instance.|
|false|Restart the instance and detach the Block Storage.|

### Notes
- Block Storage must be in `active` state.
- Re-attaching a Block Storage volume is allowed after 3 minutes.
"""

URL_CDN_LIST_PULL_ZONES: Final[Url] = Url(URL_BASE).uri("cdns/pull-zones")
"""
### Request Methods
- `GET`: List CDN Pull Zones.
- `POST`: Create a new CDN Pull Zone.

### Request Body Schema
- `POST`:

```js
{
    "label": String, // The user-supplied label.
    "origin_scheme": String, // The URI scheme of the origin domain. Enum: ["http", "https"]
    "origin_domain": String, // The domain name from which the content stored in the CDN will be pulled.
    "vanity_domain": Optional<String>, // An optional domain name that can be used to access the cached files.
    "ssl_cert": Optional<String>, // Base 64 encoded SSL certificate (required if vanity_domain and origin_scheme=https)
    "ssl_cert_key": Optional<String>, // Base 64 encoded SSL private key (required if vanity_domain and origin_scheme=https)
    "cors": Optional<Boolean>, // Enable Cross-origin resource sharing
    "gzip": Optional<Boolean>, // Enable Gzip compression
    "block_ai": Optional<Boolean>, // Block AI bots
    "block_bad_bots": Optional<Boolean> // Block potentially malicious bots
}
// Required: label, origin_scheme, origin_domain
}
```
"""

URL_CDN_PULL_ZONE_ID: Final[Url] = Url(URL_BASE).uri("cdns/pull-zones/{pullzone-id}")
"""
### Request Methods
- `GET`: Get information about a CDN Pull Zones.
- `PUT`: Update information for a CDN Pullzone. All attributes are optional. If not set, the attributes will retain their original values.
- `DELETE`: Delete a CDN Pull Zone.

### Request Body Schema
- `PUT`:

```js
{
    "label": Optional<String>, // The user-supplied label.
    "vanity_domain": Optional<String>, // An optional domain name that can be used to access the cached files.
    "ssl_cert": Optional<String>, // Base 64 encoded SSL certificate (required if vanity_domain and origin_scheme=https)
    "ssl_cert_key": Optional<String>, // Base 64 encoded SSL private key (required if vanity_domain and origin_scheme=https)
    "cors": Optional<Boolean>, // Cross-origin resource sharing
    "gzip": Optional<Boolean>, // Optional feature to compress files
    "block_ai": Optional<Boolean>, // Optional feature to block AI bots
    "block_bad_bots": Optional<Boolean>, // Optional feature to block malicious bots
    "regions": Optional<Array> // List of [Region ids](#operation/list-regions) for content delivery
}
```
"""

URL_CDN_PULL_ZONE_PURGE: Final[Url] = Url(URL_BASE).uri("cdns/pull-zones/{pullzone-id}/purge")
"""
### Request Methods
- `GET`: Clears cached content on server proxies so that visitors can get the latest page versions.

**Note:** This action may only be performed once every six hours.  
**Note:** This action may take a few extra seconds to complete.
"""

URL_CDN_PUSH_ZONES: Final[Url] = Url(URL_BASE).uri("cdns/push-zones")
"""
### Request Methods
- `GET`: List CDN Push Zones.
- `POST`: Create a new CDN Push Zone.

### Request Body Schema
- `POST`:

```js
{
    "label": String, // The user-supplied label.
    "vanity_domain": Optional<String>, // An optional domain name that can be used to access the cached files.
    "ssl_cert": Optional<String>, // Base 64 encoded SSL certificate (required if vanity_domain)
    "ssl_cert_key": Optional<String>, // Base 64 encoded SSL private key (required if vanity_domain)
    "cors": Optional<Boolean>, // Enable Cross-origin resource sharing
    "gzip": Optional<Boolean>, // Enable Gzip compression
    "block_ai": Optional<Boolean>, // Block AI bots
    "block_bad_bots": Optional<Boolean> // Block potentially malicious bots
}
```
"""

URL_CDN_PUSH_ZONE_ID: Final[Url] = Url(URL_BASE).uri("cdns/push-zones/{pushzone-id}")
"""
### Request Methods
- `GET`: Get information about a CDN Push Zone.
- `PUT`: Update information for a CDN Pushzone. All attributes are optional. If not set, the attributes will retain their original values.
- `DELETE`: Delete a CDN Push Zone.

### Request Body Schema
- `PUT`:

```js
{
    "label": Optional<String>, // The user-supplied label.
    "vanity_domain": Optional<String>, // An optional domain name that can be used to access the cached files.
    "ssl_cert": Optional<String>, // Base 64 encoded SSL certificate (required if vanity_domain)
    "ssl_cert_key": Optional<String>, // Base 64 encoded SSL private key (required if vanity_domain)
    "cors": Optional<Boolean>, // Cross-origin resource sharing
    "gzip": Optional<Boolean>, // Optional feature to compress files
    "block_ai": Optional<Boolean>, // Optional feature to block AI bots
    "block_bad_bots": Optional<Boolean>, // Optional feature to block malicious bots
    "regions": Optional<Array> // List of [Region ids](#operation/list-regions) for content delivery
}
```
"""

URL_CDN_PUSH_ZONE_FILES: Final[Url] = Url(URL_BASE).uri("cdns/push-zones/{pushzone-id}/files")
"""
### Request Methods
- `GET`: Get a list of files that have been uploaded to a specific CDN Push Zones.
- `POST`: Create a presigned post endpoint that can be used to upload a file to your Push Zone.

### Request Body Schema
- `POST`:

```js
{
    "name": String, // The name of the file including extension.
    "size": Integer // The size of the file in bytes.
}
```
"""

URL_CDN_PUSH_ZONE_FILE: Final[Url] = Url(URL_BASE).uri("cdns/push-zones/{pushzone-id}/files/{file-name}")
"""
### Request Methods
- `GET`: Get information about a CDN Push Zone file.
- `DELETE`: Delete a CDN Push Zone file.

### Path Parameters
- `pushzone-id`: The [Push Zone ID](#operation/list-pushzones)
- `file-name`: The [File Name](#operation/list-pushzone-files)
"""

URL_CONTAINER_LIST: Final[Url] = Url(URL_BASE).uri("registries")
"""
### Request Methods
- `GET`: List All Container Registry Subscriptions for this account

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.
"""

URL_CONTAINER: Final[Url] = Url(URL_BASE).uri("registry")
"""
### Request Methods
- `POST`: Create a new Container Registry Subscription

### Request Body Schema
- `POST`:

```js
{
    "name": String, // "The globally unique name to reference this registry",
    "public": Boolean, // "If true, this is a publically accessible registry allowing anyone to pull from it. If false, this registry is completely private",
    "region": String, // "The name of the region you'd like to deploy this Registry in. Can get list of regions from /registry/region/list endpoint i.e. sjc",
    "plan": String, // "The key of the plan you'd like to select which dictates how much storage you're allocated and the monthly cost. Can get list of plans from /plan/list endpoint i.e. start_up"
}
```
"""

URL_CONTAINER_ID: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}")
"""
### Request Methods
- `GET`: Get a single Container Registry Subscription
- `PUT`: Update a Container Registry Subscription
- `DELETE`: Delete a Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID

### Request Body Schema
- `PUT`:

```js
{
    "public": Boolean, // "If true, this is a publically accessible registry allowing anyone to pull from it. If false, this registry is completely private",
    "plan": String, // "The key of the plan you'd like to upgrade to which dictates how much storage you're allocated and the monthly cost. Can get list of plans from /plan/list endpoint i.e. business"
}
```
"""

URL_CONTAINER_REPOSITORY: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/repositories")
"""
### Request Methods
- `GET`: List All Repositories in a Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID
"""

URL_CONTAINER_REPOSITORY_IMAGE: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/repository/{repository-image}")
"""
### Request Methods
- `GET`: Get a single Repository in a Container Registry Subscription
- `PUT`: Update a Repository in a Container Registry Subscription
- `DELETE`: Delete a Repository from a Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID
- `repository-image`: Target repository name

### Request Body Schema
- `PUT`:

```js
{
    "description": String, // "This is my super cool hello-world project"
}
```
"""

URL_CONTAINER_DOCKER_CREDENTIALS: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/docker-credentials")
"""
### Request Methods
- `OPTIONS`: Create a fresh set of Docker Credentials for this Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID

### Query parameters
- `expiry_seconds`: "The duration in seconds for which the credentials are valid (default: 0)"
- `read_write`: "If false, credentials will be read-only (default: false)"
"""

URL_CONTAINER_KUBERNETES_DOCKER_CREDENTIALS: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/docker-credentials/kubernetes")
"""
### Request Methods
- `OPTIONS`: Create a fresh set of Docker Credentials for this Container Registry Subscription and return them in a Kubernetes friendly YAML format

### Path parameters
- `registry-id`: The Container Registry Subscription ID

### Query parameters
- `expiry_seconds`: "The duration in seconds for which the credentials are valid (default: 0)"
- `read_write`: "If false, credentials will be read-only (default: false)"
- `base64_encode`: "If true, encodes the output in base64 (default: false)"
"""

URL_CONTAINER_ROBOTS: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/robots")
"""
### Request Methods
- `GET`: List All Robots in a Conainer Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID
"""

URL_CONTAINER_ROBOT: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/robot/{robot-name}")
"""
### Request Methods
- `GET`: Get a single Robot in a Container Registry Subscription
- `PUT`: Update the description, disable, duration, and add or remove access, in a Container Registry Subscription Robot
- `DELETE`: Deletes a Robot from a Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID
- `robot-name`: The Robot name

### Request Body Schema
- `PUT`:

```js
{
    "description": String, // "Robot user auto generated by Vultr - enter only what you want to update in the request body",
    "disable": Boolean, // true,
    "duration": Integer, // -1,
    "access": [
        {
            "action": String, // "pull",
            "resource":, String, // "repository",
            "effect": String, // "allow"
        },
        {
            "action": String, // "delete",
            "resource": String, // "artifact",
            "effect": String, // "deny"
        }
    ]
}
```
"""

URL_CONTAINER_ARTIFACTS: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/repository/{repository-image}/artifacts")
"""
### Request Methods
- `GET`: List All Artifacts in a Container Registry Repository

### Path parameters
- `registry-id`: The Container Registry Subscription ID
- `repository-image`: The Repository Name
"""

URL_CONTAINER_ARTIFACT: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/repository/{repository-image}/artifact/{artifact-digest}")
"""
### Request Methods
- `GET`: Get a single Artifact in a Container Registry Repository
- `DELETE`: Deletes an Artifact from a Container Registry Repository

### Path Parameters
- `registry-id`: The Container Registry Subscription ID
- `repository-image`: The Repository Name
- `artifact-digest`: The Artifact Digest
"""

URL_CONTAINER_LIST_REGIONS: Final[Url] = Url(URL_BASE).uri("registry/region/list")
"""
### Request Methods
- `GET`: List All Regions where a Container Registry can be deployed
"""

URL_CONTAINER_UPDATE_PASSWORD: Final[Url] = Url(URL_BASE).uri("registry/{registry-id}/user/password")
"""
### Request Methods
- `PUT`: Update the Container Registy Password for this Container Registry Subscription
"""

URL_CONTAINER_LIST_PLANS: Final[Url] = Url(URL_BASE).uri("registry/plan/list")
"""
### Request Methods
- `GET`: List All Plans to help choose which one is the best fit for your Container Registry
"""

URL_DATABASE_LIST_PLANS: Final[Url] = Url(URL_BASE).uri("databases/plans")
"""
### Request Methods
- `GET`: List Managed Database Plans.

### Query parameters
- `GET`:
    - `engine` - Filter by engine type\n\n* `mysql`\n* `pg`\n* `valkey`\n* `kafka`
    - `nodes` - Filter by number of nodes.
    - `region` - Filter by [Region id](#operation/list-regions).
"""

URL_DATABASE_LIST: Final[Url] = Url(URL_BASE).uri("databases")
"""
### Request Methods
- `GET`: List all Managed Databases in your account.
- `POST`: Create a new Managed Database in a `region` with the desired `plan`. Supply optional attributes as desired.

### Query parameters
- `GET`:
    - `label` - Filter by label.
    - `tag` - Filter by specific tag.
    - `region` - Filter by [Region id](#operation/list-regions).

### Request Body Schema
- `POST`:

```js
{
    "database_engine": String, // The database engine type for the Managed Database. * `mysql` * `pg` * `valkey` * `kafka`
    "database_engine_version": String, // The version of the chosen database engine type for the Managed Database. * MySQL: `8` * PostgreSQL: `13` - `16` * Valkey: `7` * Kafka: `3.7`
    "region": String, // The [Region id](#operation/list-regions) where the Managed Database is located.
    "plan": String, // The [Plan id](#operation/list-database-plans) to use when deploying this Managed Database.
    "label": String, // A user-supplied label for this Managed Database.
    "tag": Optional<String>, // The user-supplied tag for this Managed Database.
    "vpc_id": Optional<String>, // The [VPC id](#operation/list-vpcs) to use when deploying this Managed Database.
    "maintenance_dow": Optional<String>, // The day of week for routine maintenance updates. * `monday` * `tuesday` * `wednesday` * `thursday` * `friday` * `saturday` * `sunday`
    "maintenance_time": Optional<String>, // The preferred time (UTC) for routine maintenance updates in 24-hour HH:00 format
    "trusted_ips": Optional<Array<String>>, // A list of IP addresses allowed to access the Managed Database in CIDR notation
    "mysql_sql_modes": Optional<Array<String>>, // A list of SQL modes to enable (MySQL engine types only)
    "mysql_require_primary_key": Optional<Boolean>, // Require a primary key for all tables (MySQL engine types only)
    "mysql_slow_query_log": Optional<Boolean>, // Enable slow query logging (MySQL engine types only)
    "mysql_long_query_time": Optional<Integer>, // Number of seconds to denote a slow query (MySQL engine types only)
    "eviction_policy": Optional<String> // Set the data eviction policy (Valkey engine types only)
}
```
"""

URL_DATABASE_ID: Final[Url] = Url(URL_BASE).uri("databases/{database-id}")
"""
### Request Methods
- `GET`: Get information about a Managed Database.
- `PUT`: Update information for a Managed Database. All attributes are optional. If not set, the attributes will retain their original values.
- `DELETE`: Delete a Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `PUT`:

```js
{
    "region": Optional<String>, // The [Region id](#operation/list-regions) where the Managed Database is located.
    "plan": Optional<String>, // The [Plan id](#operation/list-database-plans) for this Managed Database.
    "label": Optional<String>, // A user-supplied label for this Managed Database.
    "tag": Optional<String>, // The user-supplied tag for this Managed Database.
    "vpc_id": Optional<String>, // The [VPC id](#operation/list-vpcs) for this Managed Database.
    "maintenance_dow": Optional<String>, // The day of week for routine maintenance updates
    "maintenance_time": Optional<String>, // The preferred time (UTC) for routine maintenance updates
    "cluster_time_zone": Optional<String>, // The configured time zone in TZ database format
    "trusted_ips": Optional<Array<String>>, // A list of IP addresses allowed to access the Managed Database
    "mysql_sql_modes": Optional<Array<String>>, // A list of SQL modes to enable (MySQL engine types only)
    "mysql_require_primary_key": Optional<Boolean>, // Require a primary key for all tables (MySQL engine types only)
    "mysql_slow_query_log": Optional<Boolean>, // Enable slow query logging (MySQL engine types only)
    "mysql_long_query_time": Optional<Integer>, // Number of seconds to denote a slow query (MySQL engine types only)
    "eviction_policy": Optional<String> // Set the data eviction policy (Valkey engine types only)
}
```
"""

URL_DATABASE_USAGE: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/usage")
"""
### Request Methods
- `GET`: Get disk, memory, and vCPU usage information for a Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_USERS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/users")
"""
### Request Methods
- `GET`: List all database users within the Managed Database.
- `POST`: Create a new database user within the Managed Database. Supply optional attributes as desired.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "username": String, // The username of the database user
    "password": Optional<String>, // The password for the database user (omit to auto-generate)
    "encryption": Optional<String>, // The password encryption type (MySQL engine types only) * `caching_sha2_password` * `mysql_native_password`
    "permission": Optional<String> // The permission level (Kafka engine types only) * `admin` * `read` * `write` * `readwrite`
}
```
"""

URL_DATABASE_USER: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/users/{username}")
"""
### Request Methods
- `GET`: Get information about a Managed Database user.
- `PUT`: Update database user information within a Managed Database.
- `DELETE`: Delete a database user within a Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `username` - The [database user](#operation/list-database-users).

### Request Body Schema
- `PUT`:

```js
{
    "password": String // The password for the database user (can be empty to auto-generate)
}
```
"""

URL_DATABASE_USER_ACCESS_CONTROL: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/users/{username}/access-control")
"""
### Request Methods
- `PUT`: Configure access control settings for a Managed Database user (Valkey and Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `username` - The [database user](#operation/list-database-users).

### Request Body Schema
- `PUT`:

when access control:

```js
{
    "acl_categories": Optional<Array<String>>, // ACL categories array (Valkey)
    "acl_channels": Optional<Array<String>>, // ACL channels array (Valkey)
    "acl_commands": Optional<Array<String>>, // ACL commands array (Valkey)
    "acl_keys": Optional<Array<String>> // ACL keys array (Valkey)
}
```

Or when kafka-permission:

```js
{
    "permission": Optional<String> // Kafka permissions * `admin` * `read` * `write` * `readwrite`
}
```
"""

URL_DATABASE_LOGICAL_DATABASES: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/dbs")
"""
### Request Methods
- `GET`: List all logical databases within the Managed Database (MySQL and PostgreSQL only).
- `POST`: Create a new logical database within the Managed Database (MySQL and PostgreSQL only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "name": String // The name of the logical database
}
```
"""

URL_DATABASE_LOGICAL_DATABASE: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/dbs/{db-name}")
"""
### Request Methods
- `GET`: Get information about a logical database within a Managed Database (MySQL and PostgreSQL only).
- `DELETE`: Delete a logical database within a Managed Database (MySQL and PostgreSQL only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `db-name` - The [logical database name](#operation/list-database-dbs).
"""

URL_DATABASE_TOPICS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/topics")
"""
### Request Methods
- `GET`: List all topics within the Managed Database (Kafka engine types only).
- `POST`: Create a new topic within the Managed Database (Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "name": String, // The name for the database topic
    "partitions": Integer, // The number of partitions
    "replication": Integer, // The replication factor
    "retention_hours": Integer, // The retention hours
    "retention_bytes": Integer // The retention bytes
}
```
"""

URL_DATABASE_TOPIC: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/topics/{topic-name}")
"""
### Request Methods
- `GET`: Get information about a Managed Database topic (Kafka engine types only).
- `PUT`: Update topic information within a Managed Database (Kafka engine types only).
- `DELETE`: Delete a topic within a Managed Database (Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `topic-name` - The [database topic](#operation/list-database-topics).

### Request Body Schema
- `PUT`:

```js
{
    "partitions": Integer, // "The number of partitions for the database topic.",
    "replication": Integer, // "The replication factor for the database topic.",
    "retention_hours": Integer, // "The retention hours for the database topic.",
    "retention_bytes": Integer, // "The retention bytes for the database topic."
}
```
"""

URL_DATABASE_QUOTAS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/quotas")
"""
### Request Methods
- `GET`: List all quotas within the Managed Database (Kafka engine types only).
- `POST`: Create a new quota within the Managed Database (Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "client_id": Integer, // "The client ID for the database quota. Note: Creating a new quota with the same client ID and user will overwrite the previous record.",
    "consumer_byte_rate": Integer, // "The consumer byte rate for the database quota.",
    "producer_byte_rate": Integer, // "The producer byte rate for the database quota.",
    "request_percentage": Integer, // "The CPU request percentage for the database quota.",
    "user": String, // "The [user](#operation/list-database-users) for the database quota."
}
```
"""

URL_DATABASE_MAINTENANCE: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/maintenance")
"""
### Request Methods
- `GET`: List all available version upgrades within the Managed Database.
- `POST`: Start maintenance updates for the Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_MIGRATION: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/migration")
"""
### Request Methods
- `GET`: View the status of a migration attached to the Managed Database.
- `POST`: Start a migration to the Managed Database.
- `DELETE`: Detach a migration from the Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "host": String, // "The host name of the source server.",
    "port": Integer, // "The connection port of the source server.",
    "username": String, // "The username of the source server. Uses `default` for Valkey if left empty or unset.",
    "password": String, // "The password of the source server.",
    "database": Optional<String>, // "The database of the source server. Required for MySQL/PostgreSQL engine types, but excluded for Valkey.",
    "ignored_databases": Optional<String>, // "Comma-separated list of ignored databases on the source server. Excluded for Valkey engine types.",
    "ssl": Boolean, // "The true/false value for whether SSL is needed to connect to the source server."
}
```
"""

URL_DATABASE_READ_REPLICA: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/read-replica")
"""
### Request Methods
- `POST`: Create a read-only replica node for the Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "region": String, // "The [Region id](#operation/list-regions) where the Managed Database is located.",
    "label": String, // "A user-supplied label for this Managed Database."
}
```
"""

URL_DATABASE_PROMOTE_READ_REPLICA: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/promote-read-replica")
"""
### Request Methods
- `POST`: Promote a read-only replica node to its own primary Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_BACKUPS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/backups")
"""
### Request Methods
- `GET`: Get backup information for the Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_RESTORE: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/restore")
"""
### Request Methods
- `POST`: Create a new Managed Database from a backup.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "label": String, // A user-supplied label for this Managed Database.
    "type": String, // The type of backup restoration to use for this Managed Database.
    "date": String, // The [backup date](#operation/get-backup-information) to use when restoring the Managed Database in YYYY-MM-DD date format.
    "time": String // The [backup time](#operation/get-backup-information) to use when restoring the Managed Database in HH-MM-SS time format (24-hour UTC).
}
```
"""

URL_DATABASE_FORK: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/fork")
"""
### Request Methods
- `POST`: Fork a Managed Database to a new subscription from a backup.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "label": String, // A user-supplied label for this Managed Database.
    "region": String, // The [Region id](#operation/list-regions) where the Managed Database is located.
    "plan": String, // The [Plan id](#operation/list-database-plans) to use when deploying this Managed Database.
    "vpc_id": String, // The [VPC id](#operation/list-vpcs) to use when deploying this Managed Database.
    "type": String, // The type of backup restoration to use for this Managed Database.
    "date": String, // The [backup date](#operation/get-backup-information) to use when restoring the Managed Database in YYYY-MM-DD date format.
    "time": String // The [backup time](#operation/get-backup-information) to use when restoring the Managed Database in HH-MM-SS time format (24-hour UTC).
}
```
"""

URL_DATABASE_CONNECTION_POOLS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connection-pools")
"""
### Request Methods
- `GET`: List all connection pools within the Managed Database (PostgreSQL engine types only).
- `POST`: Create a new connection pool within the Managed Database (PostgreSQL engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "name": String, // The name of the connection pool.
    "database": String, // The logical database associated with the connection pool.
    "username": String, // The database user associated with the connection pool.
    "mode": String, // The mode for the connection pool.
    "size": Integer // The size of the connection pool.
}
```
"""

URL_DATABASE_CONNECTION_POOL: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connection-pools/{pool-name}")
"""
### Request Methods
- `GET`: Get information about a Managed Database connection pool (PostgreSQL engine types only).
- `PUT`: Update connection-pool information within a Managed Database (PostgreSQL engine types only).
- `DELETE`: Delete a connection pool within a Managed Database (PostgreSQL engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `pool-name` - The [connection pool name](#operation/list-connection-pools).

### Request Body Schema
- `PUT`:

```js
{
    "database": String, // The logical database associated with the connection pool.
    "username": String, // The database user associated with the connection pool.
    "mode": String, // The mode for the connection pool.
    "size": Integer // The size of the connection pool.
}
```
"""

URL_DATABASE_ADVANCED_OPTIONS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/advanced-options")
"""
### Request Methods
- `GET`: List all configured and available advanced options for the Managed Database (MySQL, PostgreSQL, and Kafka engine types only).
- `PUT`: Updates an advanced configuration option for the Managed Database (MySQL, PostgreSQL, and Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_VERSION_UPGRADE: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/version-upgrade")
"""
### Request Methods
- `GET`: List all available version upgrades within the Managed Database (PostgreSQL engine types only).
- `POST`: Start a version upgrade for the Managed Database (PostgreSQL engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `POST`:

```js
{
    "version": String // The version number to upgrade the Managed Database to.
}
```
"""

URL_DATABASE_ALERTS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/alerts")
"""
### Request Methods
- `POST`: List service alert messages for the Managed Database.

### Request Body Schema
- `POST`: Include a JSON object in the request body with a content type of **application/json**.
"""

URL_DATABASE_AVAILABLE_CONNECTORS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/available-connectors")
"""
### Request Methods
- `GET`: List all available connectors for the Managed Database (Kafka engine types only).
"""

URL_DATABASE_AVAILABLE_CONNECTOR_CONFIGURATION: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/available-connectors/{connector-class}/configuration")
"""
### Request Methods
- `GET`: Get the configuration schema for the Managed Database connector (Kafka engine types only).
"""

URL_DATABASE_CONNECTORS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connectors")
"""
### Request Methods
- `GET`: List all connectors within the Managed Database (Kafka engine types only).
- `POST`: Create a new connector within the Managed Database (Kafka engine types only).

### Request Body Schema
- `POST`: Include a JSON object in the request body with a content type of **application/json**.
"""

URL_DATABASE_CONNECTOR: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connectors/{connector-name}")
"""
### Request Methods
- `GET`: Get information about a Managed Database connector (Kafka engine types only).
- `PUT`: Update connector information within a Managed Database (Kafka engine types only).
- `DELETE`: Delete a connector within a Managed Database (Kafka engine types only).

### Request Body Schema
- `PUT`: Include a JSON object in the request body with a content type of **application/json**.
"""

URL_DATABASE_CONNECTOR_STATUS: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connectors/{connector-name}/status")
"""
### Request Methods
- `GET`: Get status information about a Managed Database connector (Kafka engine types only).
"""

URL_DATABASE_CONNECTOR_RESTART: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connectors/{connector-name}/restart")
"""
### Request Methods
- `POST`: Restart a connector within a Managed Database (Kafka engine types only).
"""

URL_DATABASE_CONNECTOR_PAUSE: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connectors/{connector-name}/pause")
"""
### Request Methods
- `POST`: Pause a connector within a Managed Database (Kafka engine types only).
"""

URL_DATABASE_CONNECTOR_RESUME: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connectors/{connector-name}/resume")
"""
### Request Methods
- `POST`: Resume a paused connector within a Managed Database (Kafka engine types only).
"""

URL_DATABASE_CONNECTOR_TASK_RESTART: Final[Url] = Url(URL_BASE).uri("databases/{database-id}/connectors/{connector-name}/tasks/{task-id}/restart")
"""
### Request Methods
- `POST`: Restart a task within a Managed Database connector (Kafka engine types only).
"""

URL_DOMAIN_LIST: Final[Url] = Url(URL_BASE).uri("domains")
"""
### Request Methods
- `GET`: List all DNS Domains in your account.
- `POST`: Create a DNS Domain for `domain`. If no `ip` address is supplied a domain with no records will be created.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema

- `POST`:

```js
{
    "domain": String, // "Your registered DNS Domain name.",
    "ip": Optional<String>, // "The default IP address for your DNS Domain. If omitted an empty domain zone will be created.",
    "dns_sec": Optional<String>, // "Enable or disable DNSSEC.\\n\\n* enabled\\n* disabled (default)"
}
```
"""

URL_DOMAIN: Final[Url] = Url(URL_BASE).uri("domains/{dns-domain}")
"""
### Request Methods
- `GET`: Get information for the DNS Domain.
- `PUT`: Update the DNS Domain.
- `DELETE`: Delete the DNS Domain.

### Path parameters
- `dns-domain` - The [DNS Domain](#operation/list-dns-domains).

### Request Body Schema
- `PUT`:

```js
{
    "dns_sec": String, // "Enable or disable DNSSEC.\\n\\n* enabled\\n* disabled"
}
```
"""

URL_DOMAIN_SOA: Final[Url] = Url(URL_BASE).uri("domains/{dns-domain}/soa")
"""
### Request Methods
- `GET`: Get SOA information for the DNS Domain.
- `PATCH`: Update the SOA information for the DNS Domain. All attributes are optional. If not set, the attributes will retain their original values.

### Path parameters
- `dns-domain` - The [DNS Domain](#operation/list-dns-domains).

### Request Body Schema
- `PATCH`:

```js
{
    "nsprimary": String, // "Set the primary nameserver.",
    "email": String, // "Set the contact email address."
}
```
"""

URL_DOMAIN_DNSSEC: Final[Url] = Url(URL_BASE).uri("domains/{dns-domain}/dnssec")
"""
### Request Methods
- `GET`: Get the DNSSEC information for the DNS Domain.

### Path parameters
- `dns-domain` - The [DNS Domain](#operation/list-dns-domains).
"""

URL_DOMAIN_RECORDS: Final[Url] = Url(URL_BASE).uri("domains/{dns-domain}/records")
"""
### Request Methods
- `GET`: Get the DNS records for the Domain.
- `POST`: Create a DNS record.

### Path parameters
- `dns-domain` - The [DNS Domain](#operation/list-dns-domains).

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "name": String, // "The hostname for this DNS record.",
    "type": String, // "The DNS record type.\\n\\n* A\\n* AAAA\\n* CNAME\\n* NS\\n* MX\\n* SRV\\n* TXT\\n* CAA\\n* SSHFP",
    "data": String, // "The DNS data for this record type.",
    "ttl": Integer // "Time to Live in seconds.",
    "priority": Integer // "DNS priority. Does not apply to all record types. (Only required for MX and SRV)"
}
```
"""

URL_DOMAIN_RECORD: Final[Url] = Url(URL_BASE).uri("domains/{dns-domain}/records/{record-id}")
"""
### Request Methods
- `GET`: Get information for a DNS Record.
- `PATCH`: Update the information for a DNS record. All attributes are optional. If not set, the attributes will retain their original values.
- `DELETE`: Delete the DNS record.

### Path parameters
- `dns-domain` - The [DNS Domain](#operation/list-dns-domains).
- `record-id` - The [DNS Record id](#operation/list-dns-domain-records).

### Request Body Schema
- `PATCH`:

```js
{
    "name": String // "The hostname for this DNS record.",
    "data": String // "The DNS data for this record type.",
    "ttl": Integer // "Time to Live in seconds.",
    "priority": Integer // "DNS priority. Does not apply to all record types."
}
```
"""

URL_FIREWALL_GROUP_LIST: Final[Url] = Url(URL_BASE).uri("firewalls")
"""
### Request Methods
- `GET`: Get a list of all Firewall Groups.
- `POST`: Create a new Firewall Group.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "description": String, // "User-supplied description of this Firewall Group."
}
```
"""

URL_FIREWALL_GROUP_ID: Final[Url] = Url(URL_BASE).uri("firewalls/{firewall-group-id}")
"""
### Request Methods
- `GET`: Get information for a Firewall Group.
- `PUT`: Update information for a Firewall Group.
- `DELETE`: Delete a Firewall Group.

### Path parameters
- `firewall-group-id` - The [Firewall Group id](#operation/list-firewall-groups).

### Request Body Schema
- `PUT`:

```js
{
    "description": String, // "User-supplied description of this Firewall Group."
}
```
"""

URL_FIREWALL_GROUP_RULES: Final[Url] = Url(URL_BASE).uri("firewalls/{firewall-group-id}/rules")
"""
### Request Methods
- `GET`: Get the Firewall Rules for a Firewall Group.
- `POST`: Create a Firewall Rule for a Firewall Group. The attributes `ip_type`, `protocol`, `subnet`, and `subnet_size` are required.

### Path parameters
- `firewall-group-id` - The [Firewall Group id](#operation/list-firewall-groups).

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "ip_type": String, // "The type of IP rule.\\n\\n* v4\\n* v6",
    "protocol": String, // "The protocol for this rule.\\n\\n* ICMP\\n* TCP\\n* UDP\\n* GRE\\n* ESP\\n* AH\\n",
    "subnet": String, // "IP address representing a subnet. The IP address format must match with the \"ip_type\" parameter value.",
    "subnet_size": Integer, // "The number of bits for the netmask in CIDR notation. Example: 32",
    "port": Optional<String>, // "TCP/UDP only. This field can be a specific port or a colon separated port range.",
    "source": Optional<String>, // "If the source string is given a value of \"cloudflare\" subnet and subnet_size will both be ignored.\\nPossible values:\\n\\n|   | Value | Description |\\n| - | ------ | ------------- |\\n|   | \"\" | Use the value from `subnet` and `subnet_size`. |\\n|   | cloudflare | Allow all of Cloudflare's IP space through the firewall |\\n|   | [Load Balancer id](#operation/list-load-balancers) | Provide a load balancer ID to use its IPs |\\n",
    "notes": Optional<String>, // "User-supplied notes for this rule."
}
```
"""

URL_FIREWALL_GROUP_RULE: Final[Url] = Url(URL_BASE).uri("firewalls/{firewall-group-id}/rules/{firewall-rule-id}")
"""
### Request Methods
- `GET`: Get a Firewall Rule.
- `DELETE`: Delete a Firewall Rule.

### Path parameters
- `firewall-group-id` - The [Firewall Group id](#operation/list-firewall-groups).
- `firewall-rule-id` - The [Firewall Rule id](#operation/list-firewall-group-rules).
"""

URL_ISO_LIST: Final[Url] = Url(URL_BASE).uri("iso")
"""
### Request Methods
- `GET`: List all private ISOs currently available on your account.
- `POST`: Create a new private ISO. The `url` attribute is required.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "url": String // The URL from which the ISO will be downloaded.
}
```
"""

URL_ISO_ID: Final[Url] = Url(URL_BASE).uri("iso/{iso-id}")
"""
### Request Methods
- `GET`: Get information for an ISO.
- `DELETE`: Delete an ISO.

### Path parameters
- `iso-id` - The [ISO id](#operation/list-isos).
"""

URL_ISO_PUBLIC_LIST: Final[Url] = Url(URL_BASE).uri("iso-public")
"""
### Request Methods
- `GET`: List all public ISOs available.
"""

URL_INFERENCE_LIST: Final[Url] = Url(URL_BASE).uri("inference")
"""
### Request Methods
- `GET`: List all Serverless Inference subscriptions in your account.
- `POST`: Create a new Serverless Inference subscription.

### Request Body Schema
- `POST`:

```js
{
    "label": String, "A user-supplied label for this Serverless Inference subscription."
}
```
"""

URL_INFERENCE_ID: Final[Url] = Url(URL_BASE).uri("inference/{inference-id}")
"""
### Request Methods
- `GET`: Get information about a Serverless Inference subscription.
- `PATCH`: Update information for a Serverless Inference subscription.
- `DELETE`: Delete a Serverless Inference subscription.

### Path parameters
- `inference-id` - The [Inference ID](#operation/list-inference).

### Request Body Schema
- `PATCH`:

```js
{
    "label": String, // "A user-supplied label for this Serverless Inference subscription."
}
```
"""

URL_INFERENCE_USAGE: Final[Url] = Url(URL_BASE).uri("inference/{inference-id}/usage")
"""
### Request Methods
- `GET`: Get usage information for a Serverless Inference subscription.

### Path parameters
- `inference-id` - The [Inference ID](#operation/list-inference).
"""

URL_INSTANCE_LIST: Final[Url] = Url(URL_BASE).uri("instances")
"""
### Request Methods
- `GET`: List all VPS instances in your account.

### Query Parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
- `tag` - Filter by specific tag. (Deprecated)
- `label` - Filter by label.
- `main_ip` - Filter by main ip address.
- `region` - Filter by [Region id](#operation/list-regions).
- `firewall_group_id` - Filter by [Firewall group id](#operation/list-firewall-groups).
- `hostname` - Filter by hostname.
- `show_pending_charges` - Set to `true` to show pending charges.
"""

URL_INSTANCE_CREATE: Final[Url] = Url(URL_BASE).uri("instances")
"""
### Request Methods
- `POST`: Create a new VPS Instance in a `region` with the desired `plan`. Choose one of the following to deploy the instance:
    - `os_id`
    - `iso_id`
    - `snapshot_id`
    - `app_id`
    - `image_id`

### Request Body Schema
- `POST`:

```js
{
    "region": String, // [Required] [Region id](#operation/list-regions) where the Instance is located.
    "plan": String, // [Required] [Plan id](#operation/list-plans) to use when deploying this instance.
    "os_id": Optional<Integer>, // [Operating System id](#operation/list-os) to use when deploying this instance.
    "ipxe_chain_url": Optional<String>, // URL location of the iPXE chainloader.
    "iso_id": Optional<String>, // [ISO id](#operation/list-isos) to use when deploying this instance.
    "script_id": Optional<String>, // [Startup Script id](#operation/list-startup-scripts) to use.
    "snapshot_id": Optional<String>, // [Snapshot id](#operation/list-snapshots) to use for deployment.
    "enable_ipv6": Optional<Boolean>, // Enable IPv6. Default: false
    "disable_public_ipv4": Optional<Boolean>, // Disable public IPv4 when IPv6 is enabled. Default: false
    "attach_private_network": Optional<Array<String>>, // [Deprecated] Use `attach_vpc`. [Private Network ids](#operation/list-networks).
    "attach_vpc": Optional<Array<String>>, // [VPC IDs](#operation/list-vpcs) to attach.
    "attach_vpc2": Optional<Array<String>>, // [VPC 2.0 IDs](#operation/list-vpc2) to attach.
    "label": Optional<String>, // User-supplied label (max 255 characters).
    "sshkey_id": Optional<Array<String>>, // [SSH Key ids](#operation/list-ssh-keys) to install.
    "backups": Optional<String>, // Enable automatic backups. Values: "enabled"|"disabled".
    "app_id": Optional<Integer>, // [Application id](#operation/list-applications) for deployment.
    "image_id": Optional<String>, // [Application image_id](#operation/list-applications) for deployment.
    "user_data": Optional<String>, // Base64-encoded user data (cloud-init).
    "ddos_protection": Optional<Boolean>, // Enable DDoS protection. Default: false
    "activation_email": Optional<Boolean>, // Send deployment email. Default: false
    "hostname": Optional<String>, // Hostname (max 255 characters).
    "tag": Optional<String>, // [Deprecated] Use `tags`. User-supplied tag.
    "firewall_group_id": Optional<String>, // [Firewall Group id](#operation/list-firewall-groups) to attach.
    "reserved_ipv4": Optional<String>, // [Reserved IP id](#operation/list-reserved-ips) to use as main IP.
    "enable_private_network": Optional<Boolean>, // [Deprecated] Use `enable_vpc`. Enable private networking.
    "enable_vpc": Optional<Boolean>, // Enable VPC support. Default: false
    "enable_vpc2": Optional<Boolean>, // Enable VPC 2.0 support. Default: false
    "tags": Optional<Array<String>>, // Tags to apply (max 5 tags, 255 chars each).
    "user_scheme": Optional<String>, // Linux user scheme. Values: "root"|"limited".
    "app_variables": Optional<Object> // [App variables](#operation/list-marketplace-app-variables) (key/value pairs).
}
```
"""

URL_INSTANCE_BY_ID: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}")
"""
### Request Methods
- `GET`: Get information about an Instance.
- `PATCH`: Update information for an Instance. All attributes are optional. If not set, the attributes will retain their original values.
- `DELETE`: Delete an Instance.

### Path Parameters
- `instance-id` - The [Instance ID](#operation/list-instances).

### Request Body Schema
- `PATCH`:

```js
{
    "app_id": Optional<Integer>, // [Application id](#operation/list-applications) to reinstall the instance.
    "image_id": Optional<String>, // [Application image_id](#operation/list-applications) to reinstall the instance.
    "backups": Optional<String>, // Enable automatic backups. Values: "enabled"|"disabled".
    "firewall_group_id": Optional<String>, // [Firewall Group id](#operation/list-firewall-groups) to attach.
    "enable_ipv6": Optional<Boolean>, // Enable IPv6. Default: false
    "os_id": Optional<Integer>, // [ISO id](#operation/list-isos) to reinstall (field name may be misleading).
    "user_data": Optional<String>, // Base64-encoded user data (cloud-init).
    "tag": Optional<String>, // [Deprecated] Use `tags`. User-supplied tag.
    "plan": Optional<String>, // [Plan id](#operation/list-plans) for upgrade.
    "ddos_protection": Optional<Boolean>, // Enable DDoS protection. Values: true|false.
    "attach_private_network": Optional<Array<String>>, // [Deprecated] Use `attach_vpc`. [Private Network ids](#operation/list-networks).
    "attach_vpc": Optional<Array<String>>, // [VPC IDs](#operation/list-vpcs) to attach.
    "attach_vpc2": Optional<Array<String>>, // [VPC 2.0 IDs](#operation/list-vpc2) to attach.
    "detach_private_network": Optional<Array<String>>, // [Deprecated] Use `detach_vpc`. [Private Network ids](#operation/list-networks).
    "detach_vpc": Optional<Array<String>>, // [VPC IDs](#operation/list-vpcs) to detach.
    "detach_vpc2": Optional<Array<String>>, // [VPC 2.0 IDs](#operation/list-vpc2) to detach.
    "enable_private_network": Optional<Boolean>, // [Deprecated] Use `enable_vpc`. Enable private networking.
    "enable_vpc": Optional<Boolean>, // Enable VPC support. Default: false
    "enable_vpc2": Optional<Boolean>, // Enable VPC 2.0 support. Default: false
    "label": Optional<String>, // User-supplied label (max 255 characters).
    "tags": Optional<Array<String>>, // Tags to apply (max 5 tags, 255 chars each).
    "user_scheme": Optional<String> // Linux user scheme. Values: "root"|"limited".
}
```
"""

URL_INSTANCE_REINSTALL: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/reinstall")
"""
### Request Methods
- `POST`: Reinstall an Instance using an optional `hostname`.

### Request Body Schema
- `POST`:

```js
{
    "hostname": Optional<String> // The hostname to use when reinstalling this instance.
}
```
"""

URL_INSTANCE_BANDWIDTH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/bandwidth")
"""
### Request Methods
- `GET`: Get bandwidth information about an Instance.

### Query Parameters
- `date_range` - The range of days to include (1-180). Default 30.
"""

URL_INSTANCE_NEIGHBORS: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/neighbors")
"""
### Request Methods
- `GET`: Get a list of other instances in the same location as this Instance.
"""

URL_INSTANCE_PRIVATE_NETWORKS: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/private-networks")
"""
### Request Methods
- `GET`: **Deprecated**: use [List Instance VPCs](#operation/list-instance-vpcs) instead. List the private networks for an Instance.

### Query Parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_INSTANCE_VPCS: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/vpcs")
"""
### Request Methods
- `GET`: List the VPCs for an Instance.

### Query Parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_INSTANCE_VPC2S: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/vpc2")
"""
### Request Methods
- `GET`: List the VPC 2.0 networks for an Instance.

### Query Parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_INSTANCE_ISO: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/iso")
"""
### Request Methods
- `GET`: Get the ISO status for an Instance.

### Path Parameters
- `instance-id` - The [Instance ID](#operation/list-instances).
"""

URL_INSTANCE_ISO_ATTACH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/iso/attach")
"""
### Request Methods
- `POST`: Attach an ISO to an Instance.

### Request Body Schema
- `POST`:

```js
{
    "iso_id": String // The [ISO id](#operation/list-isos) to attach to this Instance.
}
```
"""

URL_INSTANCE_ISO_DETACH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/iso/detach")
"""
### Request Methods
- `POST`: Detach the ISO from an Instance.

### Request Body Schema
- `POST`:

```js
{
    "network_id": String // The [Private Network id](#operation/list-networks) to detach from this Instance.
}
```
"""

URL_INSTANCE_PRIVATE_NETWORKS_ATTACH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/private-networks/attach")
"""
### Request Methods
- `POST`: Attach Private Network to an Instance. (Deprecated)

### Request Body Schema
- `POST`:

```js
{
    "network_id": String // The [Private Network id](#operation/list-networks) to attach to this Instance.
}
```
"""

URL_INSTANCE_PRIVATE_NETWORKS_DETACH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/private-networks/detach")
"""
### Request Methods
- `POST`: Detach Private Network from an Instance. (Deprecated)

### Request Body Schema
- `POST`:

```js
{
    "network_id": String // The [Private Network id](#operation/list-networks) to detach from this Instance.
}
```
"""

URL_INSTANCE_VPCS_ATTACH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/vpcs/attach")
"""
### Request Methods
- `POST`: Attach a VPC to an Instance.

### Request Body Schema
- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpcs) to attach to this Instance.
}
```
"""

URL_INSTANCE_VPCS_DETACH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/vpcs/detach")
"""
### Request Methods
- `POST`: Detach a VPC from an Instance.

### Request Body Schema
- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpcs) to detach from this Instance.
}
```
"""

URL_INSTANCE_VPC2_ATTACH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/vpc2/attach")
"""
### Request Methods
- `POST`: Attach a VPC 2.0 Network to an Instance.

### Request Body Schema
- `POST`:

```js
{
    "vpc_id": String, // The [VPC ID](#operation/list-vpc2) to attach to this Instance.
    "ip_address": Optional<String> // The IP address to use for this instance on the attached VPC 2.0 network.
}
```
"""

URL_INSTANCE_VPC2_DETACH: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/vpc2/detach")
"""
### Request Methods
- `POST`: Detach a VPC 2.0 Network from an Instance.

### Request Body Schema
- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpc2) to detach from this Instance.
}
```
"""

URL_INSTANCE_BACKUP_SCHEDULE: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/backup-schedule")
"""
### Request Methods
- `GET`: Get the backup schedule for an Instance.
- `POST`: Set the backup schedule for an Instance in UTC.

### Request Body Schema
- `POST`:

```js
{
    "type": String, // Type of backup schedule: `daily`, `weekly`, `monthly`, `daily_alt_even`, `daily_alt_odd`.
    "hour": Optional<Integer>, // Hour of day to run in UTC.
    "dow": Optional<Integer>, // Day of week to run (1-7).
    "dom": Optional<Integer> // Day of month to run (1-28).
}
```

|Type | Description |
|---|---|
|daily | Backups run every day. |
|weekly | Backups run every week. |
|monthly | Backups run every month. |
|daily_alt_even | Backups run every other day starting on an even day of the month. |
|daily_alt_odd | Backups run every other day starting on an odd day of the month |

"""

URL_INSTANCE_RESTORE: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/restore")
"""
### Request Methods
- `POST`: Restore an Instance from either `backup_id` or `snapshot_id`.

### Request Body Schema
- `POST`:

```js
{
    "backup_id": Optional<String>, // The [Backup id](#operation/list-backups) used to restore this instance.
    "snapshot_id": Optional<String> // The [Snapshot id](#operation/list-snapshots) used to restore this instance.
}
```
"""

URL_INSTANCE_IPV4: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/ipv4")
"""
### Request Methods
- `GET`: List the IPv4 information for an Instance.
- `POST`: Create an IPv4 address for an Instance.

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).

### Query Parameters
- `GET`:
    - `public_network` - If `true`, includes information about the public network adapter (such as MAC address) with the `main_ip` entry.
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "reboot": Optional<Boolean> // Set if the server is rebooted immediately after the IPv4 address is created.
}
```
"""

URL_INSTANCE_IPV6: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/ipv6")
"""
### Request Methods
- `GET`: Get the IPv6 information for an VPS Instance.

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).
"""

URL_INSTANCE_IPV4_REVERSE: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/ipv4/reverse")
"""
### Request Methods
- `POST`: Create a reverse IPv4 entry for an Instance. The `ip` and `reverse` attributes are required. 

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).

### Request Body Schema
- `POST`:

```js
{
    "ip": String, // The IPv4 address.
    "reverse": String // The IPv4 reverse entry.
}
```
"""

URL_INSTANCE_IPV6_REVERSE: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/ipv6/reverse")
"""
### Request Methods
- `GET`: List the reverse IPv6 information for an Instance.
- `POST`: Create a reverse IPv6 entry for an Instance. The `ip` and `reverse` attributes are required. IP address must be in full, expanded format.

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).

### Request Body Schema
- `POST`:

```js
{
    "ip": String, // The IPv6 address in full, expanded format.
    "reverse": String // The IPv6 reverse entry.
}
```

"""

URL_INSTANCE_IPV4_REVERSE_DEFAULT: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/ipv4/reverse/default")
"""
### Request Methods
- `POST`: Set a reverse DNS entry for an IPv4 address

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).

### Request Body Schema
- `POST`:

```js
{
    "ip": String // The IPv4 address.
}
```
"""

URL_INSTANCE_IPV6_REVERSE_IPV6: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/ipv6/reverse/{ipv6}")
"""
### Request Methods
- `DELETE`: Delete the reverse IPv6 for an Instance.

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).
- `ipv6` - The IPv6 address.
"""

URL_INSTANCE_HALT: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/halt")
"""
### Request Methods
- `POST`: Halt an Instance.

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).
"""

URL_INSTANCE_USER_DATA: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/user-data")
"""
### Request Methods
- `GET`: Get the user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) for an Instance.

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).
"""

URL_INSTANCE_UPGRADES: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/upgrades")
"""
### Request Methods
- `GET`: Get available upgrades for an Instance.

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).

### Query parameters
- `type` - Filter upgrade by type:\n\n- all (applications, os, plans)\n- applications\n- os\n- plans
"""

URL_INSTANCES_REBOOT: Final[Url] = Url(URL_BASE).uri("instances/reboot")
"""
### Request Methods
- `POST`: Reboot multiple Vultr Instances.

### Request Body Schema
- `POST`:

```js
{
    "instance_ids": Array<String> // Array of Instance ids to reboot.
}
```
"""

URL_INSTANCES_START: Final[Url] = Url(URL_BASE).uri("instances/start")
"""
### Request Methods
- `POST`: Start multiple Vultr Instances.

### Request Body Schema
- `POST`:

```js
{
    "instance_ids": Array<String> // Array of Instance ids to start.
}
```
"""

URL_INSTANCE_START: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/start")
"""
### Request Methods
- `POST`: Start an Instance.

### Path Parameters
- `instance-id` - The [Instance ID](#operation/list-instances).
"""

URL_INSTANCES_HALT: Final[Url] = Url(URL_BASE).uri("instances/halt")
"""
### Request Methods
- `POST`: Halt Instances.
"""

URL_INSTANCE_REBOOT: Final[Url] = Url(URL_BASE).uri("instances/{instance-id}/reboot")
"""
### Request Methods
- `POST`: Reboot an Instance.

### Path parameters
- `instance-id` - The [Instance ID](#operation/list-instances).
"""

URL_KUBERNETES_LIST: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters")
"""
### Request Methods
- `GET`: List all Kubernetes clusters currently deployed.
- `POST`: Create Kubernetes Cluster.

### Request Body Schema
- `POST`:

```js
{
    "label": String, // The label for your Kubernetes cluster.
    "region": String, // Region you want to deploy VKE in. See [Regions](#tag/region) for more information.
    "version": String, // Version of Kubernetes you want to deploy.
    "ha_controlplanes": Optional<Boolean>, // Whether a highly available control planes configuration should be deployed.
    "enable_firewall": Optional<Boolean>, // Whether a [Firewall Group](#tag/firewall) should be deployed and managed by this cluster.
    "node_pools": Array<{ // Array of node pool objects containing:
        "node_quantity": Integer, // Number of instances to deploy in this nodepool.
        "label": String, // Label for this nodepool.
        "plan": String, // Plan you want this nodepool to use.
        "tag": String, // Tag for node pool.
        "auto_scaler": Boolean, // Option to use the auto scaler.
        "min_nodes": Integer, // Auto scaler minimum nodes.
        "max_nodes": Integer // Auto scaler maximum nodes.
    }>
}
```
"""

URL_KUBERNETES_ID: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}")
"""
### Request Methods
- `GET`: Get Kubernetes Cluster.
- `PUT`: Update Kubernetes Cluster.
- `DELETE`: Delete Kubernetes Cluster.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).

### Request Body Schema
- `PUT`:

```js
{
    "label": Optional<String> // Label for the Kubernetes cluster.
}
```
"""

URL_KUBERNETES_DELETE_WITH_LINKED_RESOURCES: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/delete-with-linked-resources")
"""
### Request Methods
- `DELETE`: Delete Kubernetes Cluster and all related resources.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).
"""

URL_KUBERNETES_RESOURCES: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/resources")
"""
### Request Methods
- `GET`: Get the block storage volumes and load balancers deployed by the specified Kubernetes cluster.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).
"""

URL_KUBERNETES_AVAILABLE_UPGRADES: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/available-upgrades")
"""
### Request Methods
- `GET`: Get the available upgrades for the specified Kubernetes cluster.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).
"""

URL_KUBERNETES_UPGRADES: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/upgrades")
"""
### Request Methods
- `POST`: Start a Kubernetes cluster upgrade.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).

### Request Body Schema
- `POST`:

```js
{
    "upgrade_version": String // The version you're upgrading to.
}
```
"""

URL_KUBERNETES_NODEPOOLS: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/node-pools")
"""
### Request Methods
- `GET`: List all available NodePools on a Kubernetes Cluster.
- `POST`: Create NodePool for a Existing Kubernetes Cluster.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).

### Request Body Schema
- `POST`:

```js
{
    "node_quantity": Integer, // Number of instances in this nodepool.
    "label": String, // Label for the nodepool.
    "plan": String, // Plan that this nodepool will use.
    "tag": Optional<String>, // Tag for node pool.
    "auto_scaler": Optional<Boolean>, // Option to use the auto scaler.
    "min_nodes": Optional<Integer>, // Auto scaler minimum nodes.
    "max_nodes": Optional<Integer>, // Auto scaler maximum nodes.
    "labels": Optional<Object> // Map of key/value pairs defining labels.
}
```
"""

URL_KUBERNETES_NODEPOOL: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}")
"""
### Request Methods
- `GET`: Get Nodepool from a Kubernetes Cluster.
- `PATCH`: Update a Nodepool on a Kubernetes Cluster.
- `DELETE`: Delete a NodePool from a Kubernetes Cluster.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).
- `nodepool-id` - The [NodePool ID](#operation/get-nodepools).

### Request Body Schema
- `PATCH`:

```js
{
    "node_quantity": Integer, // Number of instances in the NodePool.
    "tag": Optional<String>, // Tag for node pool.
    "auto_scaler": Optional<Boolean>, // Option to use the auto scaler.
    "min_nodes": Optional<Integer>, // Auto scaler minimum nodes.
    "max_nodes": Optional<Integer>, // Auto scaler maximum nodes.
    "labels": Optional<Object> // Map of key/value pairs defining labels.
}
```
"""

URL_KUBERNETES_NODEPOOL_INSTANCE: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id}")
"""
### Request Methods
- `DELETE`: Delete a single nodepool instance from a given Nodepool.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).
- `nodepool-id` - The [NodePool ID](#operation/get-nodepools).
- `node-id` - The [Instance ID](#operation/list-instances).
"""

URL_KUBERNETES_NODEPOOL_INSTANCE_RECYCLE: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id}/recycle")
"""
### Request Methods
- `POST`: Recycle a specific NodePool Instance.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).
- `nodepool-id` - The [NodePool ID](#operation/get-nodepools).
- `node-id` - Node ID
"""

URL_KUBERNETES_CONFIG: Final[Url] = Url(URL_BASE).uri("kubernetes/clusters/{vke-id}/config")
"""
### Request Methods
- `GET`: Get Kubernetes Cluster Kubeconfig.

### Path parameters
- `vke-id` - The [VKE ID](#operation/list-kubernetes-clusters).
"""

URL_KUBERNETES_VERSIONS: Final[Url] = Url(URL_BASE).uri("kubernetes/versions")
"""
### Request Methods
- `GET`: Get a list of supported Kubernetes versions.
"""


URL_LOAD_BALANCER_LIST: Final[Url] = Url(URL_BASE).uri("load-balancers")
"""
### Request Methods
- `GET`: List the Load Balancers in your account.

### Query parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_LOAD_BALANCER_CREATE: Final[Url] = Url(URL_BASE).uri("load-balancers")
"""
### Request Methods
- `POST`: Create a new Load Balancer in a particular `region`.

### Request Body Schema
- `POST`:

```js
{
    "region": String, // [Required] [Region id](#operation/list-regions) to create this Load Balancer.
    "balancing_algorithm": Optional<String>, // The balancing algorithm.\n\n* roundrobin (default)\n* leastconn
    "ssl_redirect": Optional<Boolean>, // If `true`, this will redirect all HTTP traffic to HTTPS. You must have an HTTPS rule and SSL certificate installed on the load balancer to enable this option.\n\n* true\n* false
    "http2": Optional<Boolean>, // If `true`, this will enable HTTP2 traffic. You must have an HTTPS forwarding rule combo (HTTPS -> HTTPS) to enable this option.\n\n* true\n* false
    "http3": Optional<Boolean>, // If `true`, this will enable HTTP3/QUIC traffic. You must have HTTP2 enabled.\n\n* true\n* false
    "nodes": Optional<Integer>, // The number of nodes to add to the load balancer (1-99), must be an odd number. This defaults to 1.
    "proxy_protocol": Optional<Boolean>, // If `true`, you must configure backend nodes to accept Proxy protocol.\n\n* true\n* false (Default)
    "timeout": Optional<Integer>, // The maximum time allowed for the connection to remain inactive before timing out in seconds. This defaults to 600.
    "health_check": Optional<{ 
        "protocol": String, // The protocol to use for health checks.\n\n* HTTPS\n* HTTP\n* TCP
        "port": Integer, // The port to use for health checks.
        "path": Optional<String>, // HTTP Path to check. Only applies if protocol is HTTP, or HTTPS.
        "check_interval": Optional<Integer>, // Interval between health checks.
        "response_timeout": Optional<Integer>, // Timeout before health check fails.
        "unhealthy_threshold": Optional<Integer>, // Number times a check must fail before becoming unhealthy.
        "healthy_threshold": Optional<Integer> // Number of times a check must succeed before returning to healthy status.
    }>,
    "forwarding_rules": Array<{ // [Required] Array of forwarding rules
        "frontend_protocol": String, // The protocol on the Load Balancer to forward to the backend.\n\n* HTTP\n* HTTPS\n* TCP
        "frontend_port": Integer, // The port number on the Load Balancer to forward to the backend.
        "backend_protocol": String, // The protocol destination on the backend server.\n\n* HTTP\n* HTTPS\n* TCP
        "backend_port": Integer // The port number destination on the backend server.
    }>,
    "sticky_session": Optional<{
        "cookie_name": String // The cookie name to make sticky. See [Load Balancer documentation](https://www.vultr.com/docs/vultr-load-balancers/#Load_Balancer_Configuration).
    }>,
    "ssl": Optional<{
        "private_key": String, // The private key.
        "certificate": String, // The SSL certificate.
        "chain": Optional<String>, // The certificate chain.
        "private_key_b64": Optional<String>, // The private key base64 encoded. (Base64 encoded values should not be used alongside with non-Base64 encoded values)
        "certificate_b64": Optional<String>, // The SSL certificate base64 encoded. (Base64 encoded values should not be used alongside with non-Base64 encoded values)
        "chain_b64": Optional<String> // The certificate chain base64 encoded. (Base64 encoded values should not be used alongside with non-Base64 encoded values)
    }>,
    "label": Optional<String>, // Label for your Load Balancer.
    "instances": Optional<Array<String>>, // An array of instances IDs that you want attached to the load balancer.
    "firewall_rules": Optional<Array<{
        "port": Integer, // Port for this rule.
        "source": String, // If the source string is given a value of \"cloudflare\" then cloudflare IPs will be supplied. Otherwise enter a IP address with subnet size that you wish to permit through the firewall.
        "ip_type": String // The type of IP rule.\n\n* v4\n* v6
    }>>,
    "vpc": Optional<String>, // ID of the VPC you wish to use. If a VPC ID is omitted it will default to the public network.
    "auto_ssl": Optional<{
        "domain_zone": String, // The domain zone. (example.com)
        "domain_sub": Optional<String> // (optional) Subdomain to append to the domain zone.
    }>,
    "global_regions": Optional<Array<String>> // Array of [Region ids](#operation/list-regions) to deploy child Load Balancers to.
}
```
"""

URL_LOAD_BALANCER_ID: Final[Url] = Url(URL_BASE).uri("load-balancers/{load-balancer-id}")
"""
### Request Methods
- `GET`: Get information for a Load Balancer.
- `PATCH`: Update information for a Load Balancer. All attributes are optional. If not set, the attributes will retain their original values.
- `DELETE`: Delete a Load Balancer.

### Path parameters
- `load-balancer-id` - The [Load Balancer id](#operation/list-load-balancers).

### Request Body Schema
- `PATCH`:

```js
{
    "ssl": {
        "private_key": String, // "The private key.",
        "certificate": String, // "The SSL certificate.",
        "chain": String, // "The certificate chain.",
        "private_key_b64": String, // "The private key base64 encoded.",
        "certificate_b64": String, // "The SSL certificate base64 encoded.",
        "chain_b64": String, // "The certificate chain base64 encoded."
    },
    "sticky_session": {
        "cookie_name": String, // "The cookie name to make sticky."
    },
    "forwarding_rules": [{
        "frontend_protocol": String, // "The protocol on the Load Balancer to forward to the backend.\n\n* HTTP\n* HTTPS\n* TCP",
        "frontend_port": Integer, // "The port number on the Load Balancer to forward to the backend.",
        "backend_protocol": String, // "The protocol destination on the backend server.\n\n* HTTP\n* HTTPS\n* TCP",
        "backend_port": Integer, // "The port number destination on the backend server."
    }],
    "health_check": {
        "protocol": String, // "The protocol to use for health checks.\n\n* HTTPS\n* HTTP\n* TCP",
        "port": Integer, // "The port to use for health checks.",
        "path": String, // "HTTP Path to check. Only applies if protocol is HTTP, or HTTPS.",
        "check_interval": String, // "Interval between health checks.",
        "response_timeout": String, // "Timeout before health check fails.",
        "unhealthy_threshold": String, // "Number times a check must fail before becoming unhealthy.",
        "healthy_threshold": String, // "Number of times a check must succeed before returning to healthy status."
    },
    "proxy_protocol": Boolean, // "If `true`, you must configure backend nodes to accept Proxy protocol.\n\n* true\n* false (Default)",
    "timeout": Integer, // "The maximum time allowed for the connection to remain inactive before timing out in seconds. This defaults to 600.",
    "ssl_redirect": Boolean, // "If `true`, this will redirect all HTTP traffic to HTTPS.",
    "http2": Boolean, // "If `true`, this will enable HTTP2 traffic.",
    "http3": Boolean, // "If `true`, this will enable HTTP3/QUIC traffic.",
    "nodes": Integer, // "The number of nodes to add to the load balancer (1-99), must be an odd number.",
    "balancing_algorithm": String, // "The balancing algorithm.\n\n* roundrobin (default)\n* leastconn",
    "instances": Array<String>, // "Send the complete array of Instances IDs that should be attached to this Load Balancer.",
    "label": String, // "The label for your Load Balancer",
    "vpc": String, // "ID of the VPC you wish to use. If a VPC ID is omitted it will default to the public network.",
    "firewall_rules": [{
        "port": Integer, // "Port for this rule.",
        "source": String, // "If the source string is given a value of \"cloudflare\" then cloudflare IPs will be supplied.",
        "ip_type": String, // "The type of IP rule.\n\n* v4\n* v6"
    }],
    "auto_ssl": {
        "domain_zone": String, // "The domain zone. (example.com)",
        "domain_sub": String, // "(optional) Subdomain to append to the domain zone."
    },
    "global_regions": Array<String>, // "Array of [Region ids](#operation/list-regions) to deploy child Load Balancers to."
}
```
"""

URL_LOAD_BALANCER_SSL: Final[Url] = Url(URL_BASE).uri("load-balancers/{load-balancer-id}/ssl")
"""
### Request Methods
- `DELETE`: Delete a Load Balancer SSL.

### Path parameters
- `load-balancer-id` - The [Load Balancer id](#operation/list-load-balancers).
"""

URL_LOAD_BALANCER_AUTO_SSL: Final[Url] = Url(URL_BASE).uri("load-balancers/{load-balancer-id}/auto_ssl")
"""
### Request Methods
- `DELETE`: Remove a Load Balancer Auto SSL. This will not remove an ssl certificate from the load balancer.

### Path parameters
- `load-balancer-id` - The [Load Balancer id](#operation/list-load-balancers).
"""

URL_LOAD_BALANCER_FORWARDING_RULES: Final[Url] = Url(URL_BASE).uri("load-balancers/{load-balancer-id}/forwarding-rules")
"""
### Request Methods
- `GET`: List the fowarding rules for a Load Balancer.
- `POST`: Create a new forwarding rule for a Load Balancer.

### Path parameters
- `load-balancer-id` - The [Load Balancer id](#operation/list-load-balancers).

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "frontend_protocol": String, // "The protocol on the Load Balancer to forward to the backend.\n\n* HTTP\n* HTTPS\n* TCP",
    "frontend_port": Integer, // "The port number on the Load Balancer to forward to the backend.",
    "backend_protocol": String, // "The protocol destination on the backend server.\n\n* HTTP\n* HTTPS\n* TCP",
    "backend_port": Integer // "The port number destination on the backend server."
}
```
"""

URL_LOAD_BALANCER_FORWARDING_RULE: Final[Url] = Url(URL_BASE).uri("load-balancers/{load-balancer-id}/forwarding-rules/{forwarding-rule-id}")
"""
### Request Methods
- `GET`: Get information for a Forwarding Rule on a Load Balancer.
- `DELETE`: Delete a Forwarding Rule on a Load Balancer.

### Path parameters
- `load-balancer-id` - The [Load Balancer id](#operation/list-load-balancers).
- `forwarding-rule-id` - The [Forwarding Rule id](#operation/list-load-balancer-forwarding-rules).
"""

URL_LOAD_BALANCER_FIREWALL_RULES: Final[Url] = Url(URL_BASE).uri("load-balancers/{load-balancer-id}/firewall-rules")
"""
### Request Methods
- `GET`: List the firewall rules for a Load Balancer.

### Path parameters
- `load-balancer-id` - The [Load Balancer id](#operation/list-load-balancers).

### Query parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_LOAD_BALANCER_FIREWALL_RULE: Final[Url] = Url(URL_BASE).uri("load-balancers/{load-balancer-id}/firewall-rules/{firewall-rule-id}")
"""
### Request Methods
- `GET`: Get a firewall rule for a Load Balancer.

### Path parameters
- `load-balancer-id` - The [Load Balancer id](#operation/list-load-balancers).
- `firewall-rule-id` - The [Firewall Rule id](#operation/list-loadbalancer-firewall-rules).
"""

URL_MARKETPLACE_APP_VARIABLES: Final[Url] = Url(URL_BASE).uri("marketplace/apps/{image-id}/variables")
"""
### Request Methods
- `GET`: List all user-supplied variables for a Marketplace App.

### Path parameters
- `image-id` - The application's [Image ID](#operation/list-applications).
"""

URL_OS: Final[Url] = Url(URL_BASE).uri("os")
"""
### Request Methods
- `GET`: List the OS images available for installation at Vultr.

### Query parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_PLAN: Final[Url] = Url(URL_BASE).uri("plans")
"""
### Request Methods
- `GET`: Get a list of all VPS plans at Vultr.

The response is an array of JSON `plan` objects, with unique `id` with sub-fields in the general format of:

  <type>-<number of cores>-<memory size>-<optional modifier>

For example: `vc2-24c-96gb-sc1`

More about the sub-fields:

* `<type>`: The Vultr type code. For example, `vc2`, `vhf`, `vdc`, etc.
* `<number of cores>`: The number of cores, such as `4c` for "4 cores", `8c` for "8 cores", etc.
* `<memory size>`: Size in GB, such as `32gb`.
* `<optional modifier>`: Some plans include a modifier for internal identification purposes, such as CPU type or location surcharges.

> Note: This information about plan id format is for general education. Vultr may change the sub-field format or values at any time. You should not attempt to parse the plan ID sub-fields in your code for any specific purpose.

### Query parameters
- `type` - Filter the results by type.

| **Type** | **Description** |
|----------|-----------------|
| all | All available types |
| vc2 | Cloud Compute |
| vdc | Dedicated Cloud |
| vhf | High Frequency Compute |
| vhp | High Performance |
| voc | All Optimized Cloud types |
| voc-g | General Purpose Optimized Cloud |
| voc-c | CPU Optimized Cloud |
| voc-m | Memory Optimized Cloud |
| voc-s | Storage Optimized Cloud |
| vcg | Cloud GPU |
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
- `os` - Filter the results by operating system.

|   | Type | Description |
| - | ------ | ------------- |
|   | windows | All available plans that support windows |
"""

URL_PLAN_METAL: Final[Url] = Url(URL_BASE).uri("plans-metal")
"""
### Request Methods
- `GET`: Get a list of all Bare Metal plans at Vultr.

The response is an array of JSON `plan` objects, with unique `id` with sub-fields in the general format of:

  <type>-<number of cores>-<memory size>-<optional modifier>

For example: `vc2-24c-96gb-sc1`

More about the sub-fields:

* `<type>`: The Vultr type code. For example, `vc2`, `vhf`, `vdc`, etc.
* `<number of cores>`: The number of cores, such as `4c` for "4 cores", `8c` for "8 cores", etc.
* `<memory size>`: Size in GB, such as `32gb`.
* `<optional modifier>`: Some plans include a modifier for internal identification purposes, such as CPU type or location surcharges.

> Note: This information about plan id format is for general education. Vultr may change the sub-field format or values at any time. You should not attempt to parse the plan ID sub-fields in your code for any specific purpose.

### Query parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_REGION: Final[Url] = Url(URL_BASE).uri("regions")
"""
### Request Methods
- `GET`: List all Regions at Vultr.

### Query parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_REGION_ID_AVAILABLE: Final[Url] = Url(URL_BASE).uri("regions/{region-id}/availability")
"""
### Request Methods
- `GET`: Get a list of the available plans in Region `region-id`. Not all plans are available in all regions.

### Path parameters
- `region-id` - The [Region id](#operation/list-regions).

### Query parameters
- `type` - Filter the results by type.

| **Type** | **Description** |
|----------|-----------------|
| all | All available types |
| vc2 | Cloud Compute |
| vdc | Dedicated Cloud |
| vhf | High Frequency Compute |
| vhp | High Performance |
| voc | All Optimized Cloud types |
| voc-g | General Purpose Optimized Cloud |
| voc-c | CPU Optimized Cloud |
| voc-m | Memory Optimized Cloud |
| voc-s | Storage Optimized Cloud |
| vbm | Bare Metal |
| vcg | Cloud GPU |
"""

URL_RESERVED_IP: Final[Url] = Url(URL_BASE).uri("reserved-ips")
"""
### Request Methods
- `GET`: List all Reserved IPs in your account.
- `POST`: Create a new Reserved IP. The `region` and `ip_type` attributes are required.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "region": String, // The [Region id](#operation/list-regions) where the Reserved IP will be created.
    "ip_type": String, // The type of IP address.\\n\\n* v4\\n* v6
    "label": String // The user-supplied label.
}
```
"""

URL_RESERVED_IP_ID: Final[Url] = Url(URL_BASE).uri("reserved-ips/{reserved-ip}")
"""
### Request Methods
- `GET`: Get information about a Reserved IP.
- `PATCH`: Update information on a Reserved IP.
- `DELETE`: Delete a Reserved IP.

### Path parameters
- `reserved-ip` - The [Reserved IP id](#operation/list-reserved-ips).

### Request Body Schema
- `PATCH`: Include a JSON object in the request body with a content type of **application/json**.

```js
{
    "label": String // The user-supplied label.
}
```
"""

URL_RESERVED_IP_ATTACH: Final[Url] = Url(URL_BASE).uri("reserved-ips/{reserved-ip}/attach")
"""
### Path Parameters
- `reserved-ip`: The [Reserved IP id](#operation/list-reserved-ips)

### Request Methods
- `POST`: Attach a Reserved IP to an compute instance or a baremetal instance - `instance_id`.

### Request Body Schema
- `POST`: Include a JSON object in the request body with a content type of **application/json**.

```js
{
    "instance_id": String // Attach the Reserved IP to a [Compute Instance id](#operation/list-instances) or a [Bare Metal Instance id](#operation/list-baremetals).
}
```
"""

URL_RESERVED_IP_DETACH: Final[Url] = Url(URL_BASE).uri("reserved-ips/{reserved-ip}/detach")
"""
### Request Methods
- `POST`: Detach a Reserved IP.

### Path parameters
- `reserved-ip` - The [Reserved IP id](#operation/list-reserved-ips).
"""

URL_RESERVED_IP_CONVERT: Final[Url] = Url(URL_BASE).uri("reserved-ips/convert")
"""
### Request Methods
- `POST`: Convert the `ip_address` of an existing [instance](#operation/list-instances) into a Reserved IP.

### Request Body Schema
- `POST`: Include a JSON object in the request body with a content type of **application/json**.

```js
{
    "ip_address": String, // The IP address to convert.
    "label": String // A user-supplied label for this IP address.
}
```
"""

URL_SNAPSHOT_LIST: Final[Url] = Url(URL_BASE).uri("snapshots")
"""
### Request Methods
- `GET`: Get information about all Snapshots in your account.
- `POST`: Create a new Snapshot for `instance_id`.

### Query parameters
- `GET`:
    - `description` - Filter the list of Snapshots by `description`.
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "instance_id": String, // Create a Snapshot for this [Instance id](#operation/list-instances).
    "description": String // The user-supplied description of the Snapshot.
}
```
"""

URL_SNAPSHOT_ID: Final[Url] = Url(URL_BASE).uri("snapshots/{snapshot-id}")
"""
### Request Methods
- `GET`: Get information about a Snapshot.
- `PUT`: Update the description for a Snapshot.
- `DELETE`: Delete a Snapshot.

### Path parameters
- `snapshot-id` - The [Snapshot id](#operation/list-snapshots).

### Request Body Schema
- `PUT`:

```js
{
    "description": String // The user-supplied description for the Snapshot.
}
```
"""

URL_SNAPSHOT_CREATE_FROM_URL: Final[Url] = Url(URL_BASE).uri("snapshots/create-from-url")
"""
### Request Methods
- `POST`: Create a new Snapshot from a RAW image located at `url`.

### Request Body Schema
- `POST`:

```js
{
    "url": String, // The public URL containing a RAW image.
    "description": Optional<String>, // The user-supplied description of the Snapshot.
    "uefi": Optional<String> // Whether or not the snapshot uses UEFI.
}
```
"""

URL_SUBACCOUNTS: Final[Url] = Url(URL_BASE).uri("subaccounts")
"""
### Request Methods
- `GET`: List all Sub-accounts linked to your account.
- `POST`: Create a new Sub-account.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "email": String, // The email address for the Sub-account.
    "name": String, // The name for the Sub-account.
    "password": String, // The password for the Sub-account.
    "acls": Array<String> // Array of ACLs to grant the Sub-account. See [ACL documentation](https://www.vultr.com/docs/vultr-api-access-control/).
}
```
"""

URL_STARTUP_SCRIPTS: Final[Url] = Url(URL_BASE).uri("startup-scripts")
"""
### Request Methods
- `GET`: List all Startup Scripts in your account.
- `POST`: Create a new Startup Script.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "name": String, // The name of the Startup Script.
    "type": String, // The type of the Startup Script.
    // * boot
    // * pxe
    "script": String // The base64 encoded Startup Script.
}
```
"""

URL_STARTUP_SCRIPT_ID: Final[Url] = Url(URL_BASE).uri("startup-scripts/{startup-id}")
"""
### Request Methods
- `GET`: Get information for a Startup Script.
- `PATCH`: Update information for a Startup Script.
- `DELETE`: Delete a Startup Script.

### Path parameters
- `startup-id` - The [Startup Script id](#operation/list-startup-scripts).

### Request Body Schema
- `PATCH`:

```js
{
    "name": Optional<String>, // The name of the Startup Script.
    "type": Optional<String>, // The type of the Startup Script.
    // * boot
    // * pxe
    "script": Optional<String> // The base64 encoded Startup Script.
}
```
"""

URL_SSH_KEY_LIST: Final[Url] = Url(URL_BASE).uri("ssh-keys")
"""
### Request Methods
- `GET`: List all SSH Keys in your account.
- `POST`: Create a new SSH Key for use with future instances.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "name": String, // The user-supplied name for this SSH Key.
    "ssh_key": String // The SSH Key.
}
```
"""

URL_SSH_KEY_ID: Final[Url] = Url(URL_BASE).uri("ssh-keys/{ssh-key-id}")
"""
### Request Methods
- `GET`: Get information about an SSH Key.
- `PATCH`: Update an SSH Key.
- `DELETE`: Delete an SSH Key.

### Path parameters
- `ssh-key-id` - The [SSH Key id](#operation/list-ssh-keys).

### Request Body Schema
- `PATCH`:

```js
{
    "name": String, // The user-supplied name for this SSH Key.
    "ssh_key": String // The SSH Key.
}
```
"""

URL_USER_LIST: Final[Url] = Url(URL_BASE).uri("users")
"""
### Request Methods
- `GET`: Get a list of all Users in your account.
- `POST`: Create a new User. The `email`, `name`, and `password` attributes are required.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "email": String, // The User's email address.
    "name": String, // The User's name.
    "password": String, // The User's password.
    "api_enabled": Boolean, // API access is permitted for this User.\n\n* true (default)\n* false
    "acls": Array<String> // An array of permissions granted.\n\n* abuse\n* alerts\n* billing\n* dns\n* firewall\n* loadbalancer\n* manage_users\n* objstore\n* provisioning\n* subscriptions\n* subscriptions_view\n* support\n* upgrade
}
```
"""

URL_USER_ID: Final[Url] = Url(URL_BASE).uri("users/{user-id}")
"""
### Request Methods
- `GET`: Get information about a User.
- `PATCH`: Update information for a User.
- `DELETE`: Delete a User.

### Path parameters
- `user-id` - The [User id](#operation/list-users).

### Request Body Schema
- `PATCH`:

```js
{
    "email": String, // The User's email address.
    "name": String, // The User's name.
    "password": String, // The User's password.
    "api_enabled": Boolean, // API access is permitted for this User.\n\n* true (default)\n* false
    "acls": Array<String> // An array of permission granted. Valid values:\n\n* abuse\n* alerts\n* billing\n* dns\n* firewall\n* loadbalancer\n* manage_users\n* objstore\n* provisioning\n* subscriptions\n* subscriptions_view\n* support\n* upgrade
}
```
"""

URL_SUBACCOUNT_LIST: Final[Url] = Url(URL_BASE).uri("subaccounts")
"""
### Request Methods
- `GET`: Get information about all sub-accounts for your account.
- `POST`: Create a new subaccount.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "email": String, // Create a new sub-account with this email address.
    "subaccount_name": String, // Your name for this sub-account.
    "subaccount_id": String // Your ID for this sub-account.
}
```
"""

URL_VPC_LIST: Final[Url] = Url(URL_BASE).uri("vpcs")
"""
### Request Methods
- `GET`: Get a list of all VPCs in your account.
- `POST`: Create a new VPC in a `region`. VPCs should use [RFC1918 private address space](https://tools.ietf.org/html/rfc1918).

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "region": String, // Create the VPC in this [Region id](#operation/list-regions).
    "description": Optional<String>, // A description of the VPC.
    "v4_subnet": Optional<String>, // The IPv4 VPC address. For example: 10.99.0.0 *If v4_subnet_mask is specified then v4_subnet is a required field.
    "v4_subnet_mask": Optional<Integer> // The number of bits for the netmask in CIDR notation. Example: 24 *If v4_subnet is specified then v4_subnet_mask is a required field.
}
```
"""

URL_VPC_ID: Final[Url] = Url(URL_BASE).uri("vpcs/{vpc-id}")
"""
### Request Methods
- `GET`: Get information about a VPC.
- `PUT`: Update information for a VPC.
- `DELETE`: Delete a VPC.

### Path parameters
- `vpc-id` - The [VPC ID](#operation/list-vpcs).

### Request Body Schema
- `PUT`:

```js
{
    "description": String // The VPC description.
}
```
"""

URL_VPC2_LIST: Final[Url] = Url(URL_BASE).uri("vpc2")
"""
### Request Methods
- `GET`: Get a list of all VPC 2.0 networks in your account.
- `POST`: Create a new VPC 2.0 network in a `region`. VPCs should use [RFC1918 private address space](https://tools.ietf.org/html/rfc1918):

    - 10.0.0.0    - 10.255.255.255  (10/8 prefix)
    - 172.16.0.0  - 172.31.255.255  (172.16/12 prefix)
    - 192.168.0.0 - 192.168.255.255 (192.168/16 prefix)

### Request Body Schema
- `POST`:

```js
{
    "region": String, // "The [Region id](#operation/list-regions) to create the instance.",
    "description": Optional<String>"A description of the VPC. </br> Must be no longer than 255 characters and may include only letters, numbers, spaces, underscores and hyphens.",
    "ip_block": Optional<String>"The VPC subnet IP address. For example: 10.99.0.0<br><span style=\"color: red\">If a prefix_length is specified then ip_block is a required field.</span>",
    "prefix_length": Optional<Integer>"The number of bits for the netmask in CIDR notation. Example: 24<br><span style=\"color: red\">If an ip_block is specified then prefix_length is a required field.</span>"
}
```
"""

URL_VPC2_ID: Final[Url] = Url(URL_BASE).uri("vpc2/{vpc-id}")
"""
### Request Methods
- `GET`: Get information about a VPC 2.0 network.
- `PUT`: Update information for a VPC 2.0 network.
- `DELETE`: Delete a VPC 2.0 network.

### Path parameters
- `vpc-id`: The [VPC ID](#operation/list-vpcs).

### Request Body Schema
- `PUT`:

```js
{
    "description": String, // "The VPC description. </br> Must be no longer than 255 characters and may include only letters, numbers, spaces, underscores and hyphens."
}
```
"""

URL_VPC2_NODES: Final[Url] = Url(URL_BASE).uri("vpc2/{vpc-id}/nodes")
"""
### Request Methods
- `GET`: Get a list of nodes attached to a VPC 2.0 network.

### Path parameters
- `vpc-id`: The [VPC ID](#operation/list-vpcs).

### Query Parameters
- `per_page`: Number of items requested per page. Default is 100 and Max is 500.
- `cursor`: Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_VPC2_ATTACH_NODES: Final[Url] = Url(URL_BASE).uri("vpc2/{vpc-id}/nodes/attach")
"""
### Request Methods
- `POST`: Attach nodes to a VPC 2.0 network.

### Path parameters
- `vpc-id`: The [VPC ID](#operation/list-vpcs).

### Request Body Schema
- `POST`:

```js
{
    "nodes": Array<Array<String>>, // "An array of ID strings for [instances](#operation/list-instances) and [Bare Metal servers](#operation/list-baremetals) to attach as nodes to the VPC 2.0 network. A limit of 1000 nodes can be processed in a request"
}
```
"""

URL_VPC2_DETACH_NODES: Final[Url] = Url(URL_BASE).uri("vpc2/{vpc-id}/nodes/detach")
"""
### Request Methods
- `POST`: Remove nodes from a VPC 2.0 network.

### Path parameters
- `vpc-id`: The [VPC ID](#operation/list-vpcs).

### Request Body Schema
- `POST`:

```js
{
    "nodes": Array<Array<String>>, // "An array of ID strings for [nodes](#operation/list-vpc2-nodes) to detach from the VPC 2.0 network. A limit of 1000 nodes can be processed in a request"
}
```
"""


URL_VFS_REGIONS: Final[Url] = Url(URL_BASE).uri("vfs/regions")
"""
### Request Methods
- `GET`: Retrieve a list of all regions where VFS can be deployed.
"""

URL_VFS_LIST: Final[Url] = Url(URL_BASE).uri("vfs")
"""
### Request Methods
- `GET`: Retrieve a list of all VFS subscriptions for the account.
- `POST`: Create a new VFS subscription with the specified configuration.

### Request Body Schema
- `POST`:

```js
{
    "region": String, // "Region identifier where to create the VFS",
    "label": String, // "User-defined label for the VFS subscription",
    "storage_size": {
        "gb": Integer, // "Size in gigabytes for the VFS"
    },
    "disk_type": Optional<String>, // "Type of storage disk (defaults to nvme if not specified)",
    "tags": Optional<Array<String>>, // "Optional tags to apply to the VFS subscription"
}
```

### Required Fields
- `region`
- `label`
- `storage_size`
"""

URL_VFS_ID: Final[Url] = Url(URL_BASE).uri("vfs/{vfs_id}")
"""
### Request Methods
- `GET`: Retrieve a specific VFS subscription by ID.
- `PUT`: Update a VFS subscription's label or storage size.
- `DELETE`: Delete a specific VFS subscription by ID.

### Path parameters
- `vfs_id`: ID of the VFS subscription to retrieve

### Request Body Schema
- `PUT`:

```js
{
    "label": String, // "New label for the VFS subscription",
    "storage_size": {
        "gb": Integer, // "Size in gigabytes for the VFS"
    }
}
```
"""

URL_VFS_ATTACHMENTS: Final[Url] = Url(URL_BASE).uri("vfs/{vfs_id}/attachments")
"""
### Request Methods
- `GET`: Retrieve a list of all attachments for a specific VFS subscription.

### Path parameters
- `vfs_id`: ID of the VFS subscription
"""

URL_VFS_ATTACHMENT: Final[Url] = Url(URL_BASE).uri("vfs/{vfs_id}/attachments/{vps_id}")
"""
### Request Methods
- `PUT`: Attach a VPS instance to a VFS subscription.
- `GET`: Retrieve details about a specific VFS-VPS attachment.
- `DELETE`: Detach a VPS instance from a VFS subscription.

### Path parameters
- `vfs_id`: ID of the VFS subscription
- `vps_id`: ID of the VPS subscription to attach
"""

URL_OBJECT_STORAGE_LIST: Final[Url] = Url(URL_BASE).uri("object-storage")
"""
### Request Methods
- `GET`: Get a list of all Object Storage in your account.
- `POST`: Create new Object Storage. The `cluster_id` and `tier_id` attributes are required.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

### Request Body Schema
- `POST`:

```js
{
    "cluster_id": Integer, // [Required] The [Cluster id](#operation/list-object-storage-clusters) where the Object Storage will be created.
    "tier_id": Integer, // [Required] The [Tier id](#operation/list-object-storage-tiers) to use for this Object Storage.
    "label": Optional<String> // The user-supplied label.
}
```
"""

URL_OBJECT_STORAGE_ID: Final[Url] = Url(URL_BASE).uri("object-storage/{object-storage-id}")
"""
### Request Methods
- `GET`: Get information about an Object Storage.
- `PUT`: Update the label for an Object Storage.
- `DELETE`: Delete an Object Storage.

### Path parameters
- `object-storage-id` - The [Object Storage id](#operation/list-object-storages).

### Request Body Schema
- `PUT`:

```js
{
    "label": String // [Required] The user-supplied label.
}
```
"""

URL_OBJECT_STORAGE_ID_REGENERATE_KEY: Final[Url] = Url(URL_BASE).uri("object-storage/{object-storage-id}/regenerate-keys")
"""
### Request Methods
- `POST`: Regenerate the keys for an Object Storage.

### Path parameters
- `object-storage-id` - The [Object Storage id](#operation/list-object-storages).
"""

URL_OBJECT_STORAGE_CLUSTERS: Final[Url] = Url(URL_BASE).uri("object-storage/clusters")
"""
### Request Methods
- `GET`: Get a list of all Object Storage Clusters.

### Query Parameters
- `per_page` - Number of items requested per page. Default is 100 and Max is 500.
- `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""

URL_OBJECT_STORAGE_TIERS: Final[Url] = Url(URL_BASE).uri("object-storage/tiers")
"""
### Request Methods
- `GET`: Get a list of all Object Storage Tiers.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""
URL_OBJECT_STORAGE_CLUSTER_TIERS: Final[Url] = Url(URL_BASE).uri("object-storage/clusters/{cluster-id}/tiers")
"""
### Request Methods
- `GET`: Get a list of all Object Storage Tiers for a given Cluster.

### Path parameters
- `cluster-id` - The [Cluster id](#operation/list-object-storage-clusters).

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
"""
