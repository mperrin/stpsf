***************************************************
Developer Notes: Releasing a new version of STPSF
***************************************************

Prerequisites
=============

 * Is the `develop` build `passing on Github Actions? <https://github.com/spacetelescope/stpsf/actions>`_ with all desired release items included?

Releasing new data packages
===========================

 #. Run ``dev_utils/master_data_release.sh`` (details below) to make a gzipped tarred archive of the STPSF data
 #. If the new data package is **required** (meaning you can't run STPSF without it, or you can run but may get incorrect results), you must bump ``DATA_VERSION_MIN`` in ``__init__.py`` to ``(0, X, Y)``
 #. Extract the resulting data archive and check that you can run the STPSF tests with ``STPSF_PATH`` pointing to it
 #. Copy the data archive into public web space. This now means on Box. The following steps need to be performed in this sequence in order to preserve the naming conventions.
     #. Find stpsf-data-LATEST.tar.gz, and click on "more options" and "Update Version".  Choose the newest version of stpsf-data-#.#.#.tar.gz
     #. This will change the name of stpsf-data-LATEST.tar.gz to be what you just uploaded, rename the file back to "stpsf-data-LATEST.tar.gz"
     #. Upload to Box a separate version of stpsf-data-#.#.#.tar.gz shared data folder for future storage.
     #. Find minimal-stpsf-data-LATEST.tar.gz, and click on "more options" and "Update Version".  Choose the newest version of minimal-stpsf-data-#.#.#.tar.gz
     #. This will change the name of minimal-stpsf-data-LATEST.tar.gz to be what you just uploaded, rename the file back to "minimal-stpsf-data-LATEST.tar.gz"
     #. Upload to Box a separate version of minimal-stpsf-data-#.#.#.tar.gz shared data folder for future storage.
     #. Verify the shared link of stpsf-data-latest.tar.gz is the same that exists in ``docs/installation.rst`` ("copy shared link" then "link settings")

 #. A shared copy will be automatically configured in STScI Central Store with updated symlink ``/grp/jwst/ote/stpsf-data``
 #. Update the URLS in ``installation.rst`` under :ref:`data_install`

Details for using `master_data_release.sh`:
-------------------------------------------

Invoke ``dev_utils/master_data_release.sh`` one of the following ways to make a gzipped tarred archive of the STPSF data suitable for distribution.

**If you are on the Institute network:** ::

   $ cd stpsf/dev_utils/
   $ ./master_data_release.sh 0.X.Y

**If you're working from a local data root:** ::

   $ cd stpsf/dev_utils/
   $ DATAROOT="/Users/you/stpsf-data-sources/" ./make-data-sdist.sh 0.X.Y
   $ cp ./stpsf-data-0.X.Y.tar.gz /where/ever/you/want/

Releasing new versions
======================

If you are making a release for `poppy` at the same time as a release in STPSF, do that first.
Update the dependency requirement to the new version of poppy, in ``stpsf/pyproject.toml``.

When you are ready, proceed with the STPSF release as follows:

 #. Get the `develop` branch into the state that you want, including all PRs merged, updated release notes. This includes all tests passing both locally and on GitHub Actions.
 #. Tag the commit with `v<version>`, being sure to sign the tag with the `-s` option.
     * ``git tag -s v<version> -m "Release v<version>"``

 #. Push tag to github, on `develop`
 #. On github, make a PR from `develop` to `stable` (this can be done ahead of time and left open, until all individual PRs are merged into `develop`.).
 #. After verifying that PR is complete and tests pass, merge it. (Once merged, both the `stable` and `develop` branches should match).
 #. Release on Github:

     #. On Github, click on "[N] Releases".
     #. Select "Draft a new release".
     #. Specify the version number, title, and brief description of the release.
     #. Press "Publish Release".

 #. Release to PyPI. This should now happen automatically on GitHub Actions. This will be triggered by a GitHub Actions build of a tagged commit on the `stable` branch, so it will happen automatically on the prior step for the PR into `stable`.


Finishing the release
=====================

 #. Email an announcement to ``stpsf-users@maillist.stsci.edu``


